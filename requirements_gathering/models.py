from django.db import models
from django.contrib.auth.models import User

class CustomerSurvey(models.Model):
    SURVEY_STATUS = (
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=SURVEY_STATUS, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CustomerResponse(models.Model):
    survey = models.ForeignKey(CustomerSurvey, on_delete=models.CASCADE, related_name='responses')
    respondent_name = models.CharField(max_length=100)
    respondent_email = models.EmailField()
    pain_points = models.TextField(help_text="Describe your main challenges with the current shuttle system")
    desired_features = models.TextField(help_text="What features would you like to see in the new system?")
    frequency_of_use = models.CharField(max_length=50, help_text="How often do you use shuttle services?")
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response from {self.respondent_name} - {self.submission_date}"

class OperationalRequirement(models.Model):
    PRIORITY_LEVELS = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_LEVELS)
    operator_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    implementation_deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.priority} priority"

class RegulatoryCompliance(models.Model):
    COMPLIANCE_STATUS = (
        ('compliant', 'Compliant'),
        ('non_compliant', 'Non-Compliant'),
        ('in_progress', 'In Progress'),
        ('not_applicable', 'Not Applicable'),
    )

    regulation_name = models.CharField(max_length=200)
    description = models.TextField()
    authority = models.CharField(max_length=100)
    compliance_status = models.CharField(max_length=20, choices=COMPLIANCE_STATUS)
    verification_date = models.DateField()
    next_review_date = models.DateField()
    responsible_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    documentation = models.TextField(help_text="List all relevant documentation and certificates")
    action_items = models.TextField(blank=True)

    def __str__(self):
        return f"{self.regulation_name} - {self.compliance_status}"

class RequirementDocument(models.Model):
    DOCUMENT_TYPES = (
        ('survey', 'Customer Survey'),
        ('operational', 'Operational Requirement'),
        ('regulatory', 'Regulatory Document'),
    )

    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='requirements_docs/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.document_type}"