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
    list_display = ('title', 'status', 'created_date', 'created_by')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'description')

@admin.register(CustomerResponse)
class CustomerResponseAdmin(admin.ModelAdmin):
    list_display = ('respondent_name', 'survey', 'submission_date')
    list_filter = ('submission_date', 'survey')
    search_fields = ('respondent_name', 'respondent_email', 'pain_points')

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