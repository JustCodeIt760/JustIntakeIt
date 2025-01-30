from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Stakeholder(models.Model):
    STAKEHOLDER_TYPES = [
        ('PARKING_OWNER', 'Parking Lot Owner'),
        ('SHUTTLE_OPERATOR', 'Shuttle Operator'),
        ('CUSTOMER', 'Customer'),
        ('LOCAL_GOVT', 'Local Government'),
        ('BUSINESS', 'Local Business'),
        ('OTHER', 'Other'),
    ]

    INFLUENCE_LEVELS = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    stakeholder_type = models.CharField(max_length=20, choices=STAKEHOLDER_TYPES)
    influence_level = models.CharField(max_length=10, choices=INFLUENCE_LEVELS)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_stakeholder_type_display()}"

class ProjectCharter(models.Model):
    title = models.CharField(max_length=200)
    problem_statement = models.TextField()
    objectives = models.TextField()
    scope = models.TextField()
    out_of_scope = models.TextField()
    start_date = models.DateField()
    estimated_end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    project_manager = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    approval_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Requirement(models.Model):
    REQUIREMENT_TYPES = [
        ('FUNCTIONAL', 'Functional'),
        ('NON_FUNCTIONAL', 'Non-Functional'),
        ('BUSINESS', 'Business'),
        ('REGULATORY', 'Regulatory'),
    ]

    PRIORITY_LEVELS = [
        ('MUST', 'Must Have'),
        ('SHOULD', 'Should Have'),
        ('COULD', 'Could Have'),
        ('WONT', "Won't Have"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    requirement_type = models.CharField(max_length=20, choices=REQUIREMENT_TYPES)
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS)
    stakeholders = models.ManyToManyField(Stakeholder, related_name='requirements')
    acceptance_criteria = models.TextField()
    status = models.CharField(max_length=20, default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.get_requirement_type_display()}"

class Risk(models.Model):
    IMPACT_LEVELS = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    likelihood = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    impact = models.CharField(max_length=10, choices=IMPACT_LEVELS)
    mitigation_strategy = models.TextField()
    owner = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='IDENTIFIED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - Impact: {self.impact}"
