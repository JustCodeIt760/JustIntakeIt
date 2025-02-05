from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import requests
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def chat(request):
    if request.method == 'GET':
        return render(request, 'chatbot/chat.html')

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            context = data.get('context', {})

            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            api_key = os.getenv('OPENROUTER_API_KEY')
            if not api_key:
                logger.error('OpenRouter API key not found')
                return JsonResponse({'error': 'API configuration error'}, status=500)

            # Debug log for API key (mask most of it)
            masked_key = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
            logger.debug(f"Using API key: {masked_key}")

            # Build system message based on context
            system_message = "You are an AI assistant helping with a project management wizard."

            if context.get('step'):
                step_descriptions = {
                    'basic': "This step collects basic project information including title, description, and initial scope.",
                    'business_case': "This step builds the business case, including problem statement, objectives, and expected benefits.",
                    'charter': "This step creates the project charter with scope, objectives, and high-level requirements.",
                    'stakeholders': "This step analyzes project stakeholders, their interests, influence, and engagement strategies.",
                    'risks': "This step identifies and assesses project risks, their likelihood, impact, and mitigation strategies.",
                    'milestones': "This step defines key project milestones and timeline.",
                    'swot': "This step analyzes project strengths, weaknesses, opportunities, and threats.",
                    'kickoff': "This step plans the project kickoff meeting, including agenda and attendees."
                }

                system_message += f"\n\nCurrent step: {context['step']}\n{step_descriptions.get(context['step'], '')}"

            # Add form context if available
            if context.get('currentFormData'):
                system_message += "\n\nCurrent form data:"
                for field, value in context['currentFormData'].items():
                    system_message += f"\n- {field}: {value}"

            # Add field-specific context for generation
            if context.get('field'):
                field_type = context.get('fieldType', 'text')
                field_label = context.get('fieldLabel', context['field'])

                system_message += f"\n\nPlease generate appropriate content for the '{field_label}' field."
                system_message += f"\nField type: {field_type}"

                if context.get('currentFormData'):
                    system_message += "\nUse the existing form data as context to ensure the generated content is relevant and consistent."

                # Add specific instructions based on field type
                if field_type == 'select':
                    system_message += "\nProvide a concise, single-option response that would be found in a dropdown menu."
                else:
                    system_message += "\nProvide ONLY the content for the field, without any explanations or additional text."
                    if field_type == 'text':
                        system_message += "\nKeep the response concise and appropriate for a single-line text input."

            # OpenRouter API call
            headers = {
                "HTTP-Referer": "https://intake.justcodeit.ai",
                "X-Title": "JustIntakeIt Chatbot",
                "Authorization": f"Bearer {api_key}"
            }

            payload = {
                "model": "anthropic/claude-3-opus-20240229",
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ]
            }

            try:
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=30
                )

                # Log response status and headers
                logger.debug(f"API Response Status: {response.status_code}")
                logger.debug(f"API Response Headers: {dict(response.headers)}")

                if not response.ok:
                    error_content = response.text
                    logger.error(f"API Error Response: {error_content}")
                    if response.status_code == 401:
                        return JsonResponse({
                            'error': 'Authentication failed. Please check API key configuration.'
                        }, status=401)
                    elif response.status_code == 429:
                        return JsonResponse({
                            'error': 'Rate limit exceeded. Please try again later.'
                        }, status=429)
                    else:
                        return JsonResponse({
                            'error': f'API error: {error_content}'
                        }, status=response.status_code)

                response.raise_for_status()
                response_data = response.json()

                # Log successful response
                logger.debug("API call successful")

                bot_response = response_data['choices'][0]['message']['content'].strip()

                # Clean up the response for field generation
                if context.get('field'):
                    # Remove any markdown formatting
                    bot_response = bot_response.replace('`', '').replace('*', '')
                    # Remove any explanatory text
                    if ':' in bot_response:
                        bot_response = bot_response.split(':')[-1].strip()
                    # Ensure single line for text inputs
                    if context.get('fieldType') == 'text':
                        bot_response = bot_response.split('\n')[0].strip()

                return JsonResponse({'response': bot_response})

            except requests.exceptions.RequestException as e:
                logger.error(f'OpenRouter API error: {str(e)}')
                if response.status_code == 429:
                    return JsonResponse({'error': 'Rate limit exceeded. Please try again later.'}, status=429)
                elif response.status_code == 401:
                    return JsonResponse({'error': 'Authentication error'}, status=401)
                else:
                    return JsonResponse({'error': f'API error: {str(e)}'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            logger.error(f'Unexpected error: {str(e)}')
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)