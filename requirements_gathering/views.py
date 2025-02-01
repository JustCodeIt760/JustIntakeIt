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