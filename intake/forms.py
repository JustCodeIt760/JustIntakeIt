from django import forms
from .models import Stakeholder, Requirement, RequirementCategory

class StakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = ['name', 'organization', 'stakeholder_type', 'email', 'phone', 'influence_level', 'interest_level']
        widgets = {
            'influence_level': forms.RadioSelect(),
            'interest_level': forms.RadioSelect(),
        }

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['title', 'description', 'category', 'priority', 'stakeholders']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'stakeholders': forms.CheckboxSelectMultiple(),
        }