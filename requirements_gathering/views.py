from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    CustomerSurvey,
    CustomerResponse,
    OperationalRequirement,
    RegulatoryCompliance,
    RequirementDocument
)
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@login_required
def requirements_dashboard(request):
    context = {
        'customer_surveys': CustomerSurvey.objects.all().order_by('-created_date')[:5],
        'operational_requirements': OperationalRequirement.objects.all().order_by('-created_date')[:5],
        'regulatory_compliances': RegulatoryCompliance.objects.all().order_by('-verification_date')[:5],
        'recent_documents': RequirementDocument.objects.all().order_by('-uploaded_date')[:5],
    }
    return render(request, 'requirements_gathering/dashboard.html', context)

@login_required
def survey_list(request):
    surveys = CustomerSurvey.objects.all().order_by('-created_date')
    return render(request, 'requirements_gathering/survey_list.html', {'surveys': surveys})

@login_required
def operational_requirements_list(request):
    requirements = OperationalRequirement.objects.all().order_by('-created_date')
    return render(request, 'requirements_gathering/operational_requirements.html', {'requirements': requirements})

@login_required
def regulatory_compliance_list(request):
    compliances = RegulatoryCompliance.objects.all().order_by('-verification_date')
    return render(request, 'requirements_gathering/regulatory_compliance.html', {'compliances': compliances})

@login_required
def document_list(request):
    documents = RequirementDocument.objects.all().order_by('-uploaded_date')
    return render(request, 'requirements_gathering/documents.html', {'documents': documents})

@login_required
def quick_interview(request):
    return render(request, 'requirements_gathering/quick_interview.html')

@login_required
@require_http_methods(["POST"])
def save_interview(request):
    action = request.POST.get('action', 'save_draft')

    # Create or get the survey
    survey, created = CustomerSurvey.objects.get_or_create(
        created_by=request.user,
        status='draft',
        defaults={
            'title': f"Interview with {request.POST.get('respondent_name', 'Client')}",
            'description': 'Quick interview capture'
        }
    )

    # Create or update the response
    response, created = CustomerResponse.objects.get_or_create(
        survey=survey,
        respondent_email=request.POST.get('respondent_email', ''),
        defaults={
            'respondent_name': request.POST.get('respondent_name', ''),
            'pain_points': request.POST.get('pain_points', ''),
            'desired_features': request.POST.get('desired_features', ''),
            'frequency_of_use': request.POST.get('frequency_of_use', '')
        }
    )

    if not created:
        response.respondent_name = request.POST.get('respondent_name', '')
        response.pain_points = request.POST.get('pain_points', '')
        response.desired_features = request.POST.get('desired_features', '')
        response.frequency_of_use = request.POST.get('frequency_of_use', '')
        response.save()

    if action == 'auto_save':
        return JsonResponse({'status': 'saved'})
    elif action == 'complete':
        survey.status = 'completed'
        survey.save()
        return redirect('requirements_gathering:interview_success')
    else:
        return redirect('requirements_gathering:interview_list')

@login_required
def interview_success(request):
    return render(request, 'requirements_gathering/interview_success.html', {
        'message': 'Interview saved successfully!'
    })

@login_required
def interview_list(request):
    surveys = CustomerSurvey.objects.filter(created_by=request.user).order_by('-created_date')
    return render(request, 'requirements_gathering/interview_list.html', {
        'surveys': surveys
    })