from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.utils import ProgrammingError
from django.db import models
from .models import (
    Sprint,
    UserStory,
    GitRepository,
    GitBranch,
    CIPipeline,
    PipelineRun
)

@login_required
def development_dashboard(request):
    try:
        context = {
            # Sprint Information
            'active_sprint': Sprint.objects.filter(status='in_progress').first(),
            'upcoming_sprints': Sprint.objects.filter(status='planned').order_by('start_date')[:3],
            'completed_sprints': Sprint.objects.filter(status='completed').order_by('-end_date')[:3],

            # User Stories
            'backlog_stories': UserStory.objects.filter(status='backlog').order_by('-priority', '-created_date')[:5],
            'in_progress_stories': UserStory.objects.filter(status='in_progress').order_by('-updated_date')[:5],
            'completed_stories': UserStory.objects.filter(status='done').order_by('-updated_date')[:5],

            # Git & CI/CD Information
            'repositories': GitRepository.objects.all().order_by('-created_date'),
            'active_branches': GitBranch.objects.filter(status='active').order_by('-created_date')[:5],
            'recent_pipeline_runs': PipelineRun.objects.all().order_by('-started_at')[:5],

            # Summary Stats
            'total_story_points': UserStory.objects.filter(sprint__status='in_progress').aggregate(models.Sum('story_points'))['story_points__sum'] or 0,
            'total_stories': UserStory.objects.count(),
            'completed_stories_count': UserStory.objects.filter(status='done').count(),
            'active_pipelines': CIPipeline.objects.filter(status='active').count(),
        }
    except ProgrammingError:
        context = {'error': 'Database tables not yet created. Please run migrations.'}

    return render(request, 'development/dashboard.html', context)

@login_required
def development_wizard(request):
    if request.method == 'POST':
        # Handle form submissions for each step
        step = request.POST.get('step')
        if step == 'sprint':
            # Handle sprint creation
            pass
        elif step == 'story':
            # Handle user story creation
            pass
        elif step == 'repository':
            # Handle repository setup
            pass
        elif step == 'pipeline':
            # Handle pipeline configuration
            pass

    try:
        context = {
            'sprints': Sprint.objects.all().order_by('-created_date')[:5],
            'stories': UserStory.objects.all().order_by('-created_date')[:5],
            'repositories': GitRepository.objects.all().order_by('-created_date'),
            'pipelines': CIPipeline.objects.all().order_by('-created_date'),
        }
    except ProgrammingError:
        context = {'error': 'Database tables not yet created. Please run migrations.'}

    return render(request, 'development/wizard.html', context)