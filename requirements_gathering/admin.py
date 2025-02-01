from django.contrib import admin
from .models import (
    CustomerSurvey,
    CustomerResponse,
    OperationalRequirement,
    RegulatoryCompliance,
    RequirementDocument
)

@admin.register(CustomerSurvey)
class CustomerSurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'status', 'created_date', 'modified_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'

@admin.register(CustomerResponse)
class CustomerResponseAdmin(admin.ModelAdmin):
    list_display = ('respondent_name', 'respondent_email', 'survey', 'frequency_of_use', 'submission_date')
    list_filter = ('frequency_of_use', 'submission_date')
    search_fields = ('respondent_name', 'respondent_email', 'pain_points', 'desired_features')
    date_hierarchy = 'submission_date'
    raw_id_fields = ('survey',)

@admin.register(OperationalRequirement)
class OperationalRequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'operator_name', 'department', 'status')
    list_filter = ('priority', 'status', 'department')
    search_fields = ('title', 'description', 'operator_name')

@admin.register(RegulatoryCompliance)
class RegulatoryComplianceAdmin(admin.ModelAdmin):
    list_display = ('regulation_name', 'authority', 'compliance_status', 'verification_date')
    list_filter = ('compliance_status', 'authority')
    search_fields = ('regulation_name', 'description', 'authority')

@admin.register(RequirementDocument)
class RequirementDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'uploaded_date', 'uploaded_by')
    list_filter = ('document_type', 'uploaded_date')
    search_fields = ('title', 'notes')