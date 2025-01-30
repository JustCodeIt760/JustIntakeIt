from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.forms import formset_factory
from .models import (
    Project, StakeholderAnalysis, BusinessCase, ProjectCharter,
    ProjectRole, FeasibilityStudy, Risk, ProjectMilestone,
    KickoffMeeting, SWOTAnalysis
)
from .forms import (
    ProjectBasicForm, BusinessCaseForm, ProjectCharterForm,
    StakeholderAnalysisForm, RiskForm, ProjectMilestoneForm,
    SWOTAnalysisForm, KickoffMeetingForm
)

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'projects_count': Project.objects.count(),
        'recent_projects': Project.objects.order_by('-created_at')[:5],
        'stakeholders_count': StakeholderAnalysis.objects.count(),
        'risks_count': Risk.objects.count(),
        'high_risks': Risk.objects.filter(likelihood='HIGH', impact='HIGH').count(),
        'pending_milestones': ProjectMilestone.objects.filter(
            project__in=Project.objects.all()
        ).order_by('target_date')[:5],
        'pending_charters': ProjectCharter.objects.filter(approved=False).count(),
        'recent_feasibility_studies': FeasibilityStudy.objects.order_by('-created_at')[:5],
        'now': timezone.now(),
    }
    return render(request, 'project_initiation/dashboard.html', context)

@login_required
def project_wizard(request, step=None, project_id=None):
    project = None
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    steps = {
        'basic': {'form': ProjectBasicForm, 'template': 'project_basic.html'},
        'business_case': {'form': BusinessCaseForm, 'template': 'business_case.html'},
        'charter': {'form': ProjectCharterForm, 'template': 'project_charter.html'},
        'stakeholders': {'form': StakeholderAnalysisForm, 'template': 'stakeholders.html'},
        'risks': {'form': RiskForm, 'template': 'risks.html'},
        'milestones': {'form': ProjectMilestoneForm, 'template': 'milestones.html'},
        'swot': {'form': SWOTAnalysisForm, 'template': 'swot.html'},
        'kickoff': {'form': KickoffMeetingForm, 'template': 'kickoff.html'},
    }

    if not step:
        step = 'basic'

    current_step = steps[step]
    form_class = current_step['form']

    if request.method == 'POST':
        form = form_class(request.POST, instance=getattr(project, step, None))
        if form.is_valid():
            if step == 'basic':
                project = form.save(commit=False)
                project.created_by = request.user
                project.save()
                messages.success(request, 'Project basics saved successfully.')
                return redirect('project_initiation:project_wizard', step='business_case', project_id=project.id)
            else:
                instance = form.save(commit=False)
                instance.project = project
                instance.save()
                if step == 'kickoff':
                    form.save_m2m()  # Save many-to-many relationships for attendees

                next_step = get_next_step(step)
                if next_step:
                    messages.success(request, f'{step.replace("_", " ").title()} saved successfully.')
                    return redirect('project_initiation:project_wizard', step=next_step, project_id=project.id)
                else:
                    messages.success(request, 'Project initiation completed successfully!')
                    return redirect('project_initiation:dashboard')
    else:
        if project and hasattr(project, step):
            form = form_class(instance=getattr(project, step))
        else:
            form = form_class()

    # Get previous step
    previous_step = get_previous_step(step)

    context = {
        'form': form,
        'project': project,
        'current_step': step,
        'steps': steps.keys(),
        'step_title': step.replace('_', ' ').title(),
        'previous_step': previous_step,
    }

    return render(request, f'project_initiation/wizard/{current_step["template"]}', context)

def get_next_step(current_step):
    steps = ['basic', 'business_case', 'charter', 'stakeholders', 'risks', 'milestones', 'swot', 'kickoff']
    try:
        current_index = steps.index(current_step)
        if current_index < len(steps) - 1:
            return steps[current_index + 1]
    except ValueError:
        pass
    return None

def get_previous_step(current_step):
    steps = ['basic', 'business_case', 'charter', 'stakeholders', 'risks', 'milestones', 'swot', 'kickoff']
    try:
        current_index = steps.index(current_step)
        if current_index > 0:
            return steps[current_index - 1]
    except ValueError:
        pass
    return None

@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'project_initiation/project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
        'business_case': getattr(project, 'businesscase', None),
        'charter': getattr(project, 'projectcharter', None),
        'stakeholders': project.stakeholderanalysis_set.all(),
        'risks': project.risk_set.all(),
        'milestones': project.projectmilestone_set.all(),
        'swot': getattr(project, 'swotanalysis', None),
        'kickoff': getattr(project, 'kickoffmeeting', None),
    }
    return render(request, 'project_initiation/project_detail.html', context)
