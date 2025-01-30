from django import forms
from .models import (
    Project, StakeholderAnalysis, BusinessCase, ProjectCharter,
    ProjectRole, FeasibilityStudy, Risk, ProjectMilestone,
    KickoffMeeting, SWOTAnalysis
)

class ProjectBasicForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class BusinessCaseForm(forms.ModelForm):
    class Meta:
        model = BusinessCase
        fields = ['problem_statement', 'objectives', 'benefits', 'costs', 'roi_analysis', 'assumptions', 'constraints']
        widgets = {
            'problem_statement': forms.Textarea(attrs={'rows': 4}),
            'objectives': forms.Textarea(attrs={'rows': 4}),
            'benefits': forms.Textarea(attrs={'rows': 4}),
            'costs': forms.Textarea(attrs={'rows': 4}),
            'roi_analysis': forms.Textarea(attrs={'rows': 4}),
            'assumptions': forms.Textarea(attrs={'rows': 4}),
            'constraints': forms.Textarea(attrs={'rows': 4}),
        }

class ProjectCharterForm(forms.ModelForm):
    class Meta:
        model = ProjectCharter
        fields = ['purpose', 'objectives', 'scope_included', 'scope_excluded',
                 'deliverables', 'success_criteria', 'budget', 'timeline_start', 'timeline_end']
        widgets = {
            'purpose': forms.Textarea(attrs={'rows': 4}),
            'objectives': forms.Textarea(attrs={'rows': 4}),
            'scope_included': forms.Textarea(attrs={'rows': 4}),
            'scope_excluded': forms.Textarea(attrs={'rows': 4}),
            'deliverables': forms.Textarea(attrs={'rows': 4}),
            'success_criteria': forms.Textarea(attrs={'rows': 4}),
            'timeline_start': forms.DateInput(attrs={'type': 'date'}),
            'timeline_end': forms.DateInput(attrs={'type': 'date'}),
        }

class StakeholderAnalysisForm(forms.ModelForm):
    class Meta:
        model = StakeholderAnalysis
        fields = ['stakeholder_name', 'organization', 'role', 'influence',
                 'interest', 'engagement_strategy', 'communication_frequency',
                 'contact_info', 'notes']
        widgets = {
            'contact_info': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['risk_description', 'likelihood', 'impact',
                 'mitigation_strategy', 'contingency_plan']
        widgets = {
            'risk_description': forms.Textarea(attrs={'rows': 3}),
            'mitigation_strategy': forms.Textarea(attrs={'rows': 3}),
            'contingency_plan': forms.Textarea(attrs={'rows': 3}),
        }

class ProjectMilestoneForm(forms.ModelForm):
    class Meta:
        model = ProjectMilestone
        fields = ['title', 'description', 'target_date', 'deliverables', 'dependencies']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'deliverables': forms.Textarea(attrs={'rows': 3}),
            'dependencies': forms.Textarea(attrs={'rows': 3}),
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SWOTAnalysisForm(forms.ModelForm):
    class Meta:
        model = SWOTAnalysis
        fields = ['strengths', 'weaknesses', 'opportunities', 'threats', 'analysis_date']
        widgets = {
            'strengths': forms.Textarea(attrs={'rows': 4}),
            'weaknesses': forms.Textarea(attrs={'rows': 4}),
            'opportunities': forms.Textarea(attrs={'rows': 4}),
            'threats': forms.Textarea(attrs={'rows': 4}),
            'analysis_date': forms.DateInput(attrs={'type': 'date'}),
        }

class KickoffMeetingForm(forms.ModelForm):
    class Meta:
        model = KickoffMeeting
        fields = ['date', 'location', 'agenda', 'presentation_materials',
                 'meeting_notes', 'action_items', 'attendees']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'agenda': forms.Textarea(attrs={'rows': 4}),
            'presentation_materials': forms.Textarea(attrs={'rows': 4}),
            'meeting_notes': forms.Textarea(attrs={'rows': 4}),
            'action_items': forms.Textarea(attrs={'rows': 4}),
        }