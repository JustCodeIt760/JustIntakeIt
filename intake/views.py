from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stakeholder, Requirement, RequirementCategory
from .forms import StakeholderForm, RequirementForm

@login_required
def dashboard(request):
    stakeholders = Stakeholder.objects.all()
    requirements = Requirement.objects.all()
    categories = RequirementCategory.objects.all()

    context = {
        'stakeholders_count': stakeholders.count(),
        'requirements_count': requirements.count(),
        'categories_count': categories.count(),
        'recent_requirements': requirements.order_by('-created_at')[:5],
        'recent_stakeholders': stakeholders.order_by('-created_at')[:5],
    }
    return render(request, 'intake/dashboard.html', context)

@login_required
def stakeholder_list(request):
    stakeholders = Stakeholder.objects.all().order_by('-influence_level', 'name')
    return render(request, 'intake/stakeholder_list.html', {'stakeholders': stakeholders})

@login_required
def stakeholder_create(request):
    if request.method == 'POST':
        form = StakeholderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stakeholder created successfully.')
            return redirect('stakeholder_list')
    else:
        form = StakeholderForm()
    return render(request, 'intake/stakeholder_form.html', {'form': form})

@login_required
def requirement_list(request):
    requirements = Requirement.objects.all().order_by('priority', '-created_at')
    return render(request, 'intake/requirement_list.html', {'requirements': requirements})

@login_required
def requirement_create(request):
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.created_by = request.user
            requirement.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Requirement created successfully.')
            return redirect('requirement_list')
    else:
        form = RequirementForm()
    return render(request, 'intake/requirement_form.html', {'form': form})

@login_required
def requirement_detail(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    return render(request, 'intake/requirement_detail.html', {'requirement': requirement})
