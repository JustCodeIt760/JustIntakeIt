from django.db import models
from django.contrib.auth.models import User

class Stakeholder(models.Model):
    STAKEHOLDER_TYPES = [
        ('PARKING_OWNER', 'Parking Lot Owner'),
        ('SHUTTLE_OPERATOR', 'Shuttle Operator'),
        ('CUSTOMER', 'Customer'),
        ('LOCAL_GOVT', 'Local Government'),
        ('BUSINESS', 'Local Business'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    stakeholder_type = models.CharField(max_length=20, choices=STAKEHOLDER_TYPES)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    influence_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 scale
    interest_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)])   # 1-5 scale
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_stakeholder_type_display()}"

class RequirementCategory(models.Model):
    CATEGORY_TYPES = [
        ('FUNCTIONAL', 'Functional'),
        ('NON_FUNCTIONAL', 'Non-Functional'),
        ('REGULATORY', 'Regulatory'),
        ('BUSINESS', 'Business'),
    ]

    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"

    class Meta:
        verbose_name_plural = "Requirement Categories"

class Requirement(models.Model):
    PRIORITY_CHOICES = [
        ('MUST', 'Must Have'),
        ('SHOULD', 'Should Have'),
        ('COULD', 'Could Have'),
        ('WONT', "Won't Have"),
    ]

    STATUS_CHOICES = [
        ('PROPOSED', 'Proposed'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('IN_REVIEW', 'In Review'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RequirementCategory, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PROPOSED')
    stakeholders = models.ManyToManyField(Stakeholder, related_name='requirements')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.get_priority_display()}"
