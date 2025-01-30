from django.contrib import admin
from .models import (
    Project, StakeholderAnalysis, BusinessCase, ProjectCharter,
    ProjectRole, FeasibilityStudy, Risk, ProjectMilestone,
    KickoffMeeting, SWOTAnalysis
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(StakeholderAnalysis)
class StakeholderAnalysisAdmin(admin.ModelAdmin):
    list_display = ('stakeholder_name', 'organization', 'role', 'influence', 'interest', 'engagement_strategy')
    list_filter = ('influence', 'interest', 'engagement_strategy')
    search_fields = ('stakeholder_name', 'organization', 'role')

@admin.register(BusinessCase)
class BusinessCaseAdmin(admin.ModelAdmin):
    list_display = ('project', 'created_at', 'updated_at')
    search_fields = ('project__title', 'problem_statement', 'objectives')

@admin.register(ProjectCharter)
class ProjectCharterAdmin(admin.ModelAdmin):
    list_display = ('project', 'approved', 'approved_by', 'approved_date', 'timeline_start', 'timeline_end')
    list_filter = ('approved', 'timeline_start', 'timeline_end')
    search_fields = ('project__title', 'purpose', 'objectives')

@admin.register(ProjectRole)
class ProjectRoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'user', 'project')
    list_filter = ('role_name',)
    search_fields = ('role_name', 'user__username', 'project__title')

@admin.register(FeasibilityStudy)
class FeasibilityStudyAdmin(admin.ModelAdmin):
    list_display = ('project', 'technical_status', 'economic_status', 'operational_status', 'legal_status')
    list_filter = ('technical_status', 'economic_status', 'operational_status', 'legal_status')
    search_fields = ('project__title', 'recommendations')

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('project', 'risk_description', 'likelihood', 'impact', 'status', 'owner')
    list_filter = ('likelihood', 'impact', 'status')
    search_fields = ('project__title', 'risk_description', 'mitigation_strategy')

@admin.register(ProjectMilestone)
class ProjectMilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'target_date')
    list_filter = ('target_date',)
    search_fields = ('title', 'project__title', 'description')

@admin.register(KickoffMeeting)
class KickoffMeetingAdmin(admin.ModelAdmin):
    list_display = ('project', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('project__title', 'agenda', 'meeting_notes')
    filter_horizontal = ('attendees',)

@admin.register(SWOTAnalysis)
class SWOTAnalysisAdmin(admin.ModelAdmin):
    list_display = ('project', 'analysis_date')
    list_filter = ('analysis_date',)
    search_fields = ('project__title', 'strengths', 'weaknesses', 'opportunities', 'threats')
