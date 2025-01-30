from django.contrib import admin
from .models import Stakeholder, ProjectCharter, Requirement, Risk

@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'stakeholder_type', 'influence_level', 'contact_email')
    list_filter = ('stakeholder_type', 'influence_level')
    search_fields = ('name', 'organization', 'contact_email')

@admin.register(ProjectCharter)
class ProjectCharterAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'estimated_end_date', 'budget', 'approved')
    list_filter = ('approved',)
    search_fields = ('title', 'problem_statement', 'objectives')

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'requirement_type', 'priority', 'status')
    list_filter = ('requirement_type', 'priority', 'status')
    search_fields = ('title', 'description', 'acceptance_criteria')
    filter_horizontal = ('stakeholders',)

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('title', 'likelihood', 'impact', 'owner', 'status')
    list_filter = ('impact', 'status')
    search_fields = ('title', 'description', 'mitigation_strategy', 'owner')
