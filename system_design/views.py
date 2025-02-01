from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    AWSComponent,
    APIEndpoint,
    UIComponent,
    SystemIntegration,
    ArchitectureDiagram
)

@login_required
def system_design_dashboard(request):
    context = {
        'aws_components': AWSComponent.objects.all().order_by('-created_date')[:5],
        'api_endpoints': APIEndpoint.objects.all().order_by('-created_date')[:5],
        'ui_components': UIComponent.objects.all().order_by('-created_date')[:5],
        'integrations': SystemIntegration.objects.all().order_by('-created_date')[:5],
        'diagrams': ArchitectureDiagram.objects.all().order_by('-created_date')[:5],
    }
    return render(request, 'system_design/dashboard.html', context)

@login_required
def aws_component_list(request):
    components = AWSComponent.objects.all().order_by('-created_date')
    return render(request, 'system_design/aws_components.html', {'components': components})

@login_required
def api_endpoint_list(request):
    endpoints = APIEndpoint.objects.all().order_by('-created_date')
    return render(request, 'system_design/api_endpoints.html', {'endpoints': endpoints})

@login_required
def ui_component_list(request):
    components = UIComponent.objects.all().order_by('-created_date')
    return render(request, 'system_design/ui_components.html', {'components': components})

@login_required
def integration_list(request):
    integrations = SystemIntegration.objects.all().order_by('-created_date')
    return render(request, 'system_design/integrations.html', {'integrations': integrations})

@login_required
def architecture_diagram_list(request):
    diagrams = ArchitectureDiagram.objects.all().order_by('-created_date')
    return render(request, 'system_design/diagrams.html', {'diagrams': diagrams})