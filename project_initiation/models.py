from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StakeholderAnalysis(models.Model):
    INFLUENCE_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    INTEREST_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    ENGAGEMENT_STRATEGY_CHOICES = [
        ('MANAGE_CLOSELY', 'Manage Closely'),
        ('KEEP_SATISFIED', 'Keep Satisfied'),
        ('KEEP_INFORMED', 'Keep Informed'),
        ('MONITOR', 'Monitor'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    stakeholder_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    influence = models.CharField(max_length=10, choices=INFLUENCE_CHOICES)
    interest = models.CharField(max_length=10, choices=INTEREST_CHOICES)
    engagement_strategy = models.CharField(max_length=20, choices=ENGAGEMENT_STRATEGY_CHOICES)
    communication_frequency = models.CharField(max_length=100)
    contact_info = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stakeholder_name} - {self.organization}"

class BusinessCase(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    problem_statement = models.TextField()
    objectives = models.TextField()
    benefits = models.TextField()
    costs = models.TextField()
    roi_analysis = models.TextField()
    assumptions = models.TextField()
    constraints = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Business Case - {self.project.title}"

class ProjectCharter(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    purpose = models.TextField()
    objectives = models.TextField()
    scope_included = models.TextField()
    scope_excluded = models.TextField()
    deliverables = models.TextField()
    success_criteria = models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    timeline_start = models.DateField()
    timeline_end = models.DateField()
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_charters')
    approved_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Project Charter - {self.project.title}"

class ProjectRole(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)
    responsibilities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.role_name} - {self.user.get_full_name()}"

class FeasibilityStudy(models.Model):
    FEASIBILITY_STATUS_CHOICES = [
        ('FEASIBLE', 'Feasible'),
        ('NOT_FEASIBLE', 'Not Feasible'),
        ('NEEDS_INVESTIGATION', 'Needs Further Investigation'),
    ]

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    technical_feasibility = models.TextField()
    technical_status = models.CharField(max_length=20, choices=FEASIBILITY_STATUS_CHOICES)
    economic_feasibility = models.TextField()
    economic_status = models.CharField(max_length=20, choices=FEASIBILITY_STATUS_CHOICES)
    operational_feasibility = models.TextField()
    operational_status = models.CharField(max_length=20, choices=FEASIBILITY_STATUS_CHOICES)
    legal_feasibility = models.TextField()
    legal_status = models.CharField(max_length=20, choices=FEASIBILITY_STATUS_CHOICES)
    recommendations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feasibility Study - {self.project.title}"

class Risk(models.Model):
    LIKELIHOOD_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    IMPACT_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    STATUS_CHOICES = [
        ('IDENTIFIED', 'Identified'),
        ('ASSESSED', 'Assessed'),
        ('MITIGATED', 'Mitigated'),
        ('CLOSED', 'Closed'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    risk_description = models.TextField()
    likelihood = models.CharField(max_length=10, choices=LIKELIHOOD_CHOICES)
    impact = models.CharField(max_length=10, choices=IMPACT_CHOICES)
    mitigation_strategy = models.TextField()
    contingency_plan = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='IDENTIFIED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Risk - {self.risk_description[:50]}"

class ProjectMilestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_date = models.DateField()
    deliverables = models.TextField()
    dependencies = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.target_date}"

class KickoffMeeting(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    agenda = models.TextField()
    attendees = models.ManyToManyField(User)
    presentation_materials = models.TextField()
    meeting_notes = models.TextField()
    action_items = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kickoff Meeting - {self.project.title}"

class SWOTAnalysis(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    strengths = models.TextField()
    weaknesses = models.TextField()
    opportunities = models.TextField()
    threats = models.TextField()
    analysis_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SWOT Analysis - {self.project.title}"

class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Stop(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, related_name='stops', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    sequence_number = models.IntegerField()  # Order in the route
    estimated_wait_time = models.IntegerField(default=0)  # in minutes
    last_vehicle_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['route', 'sequence_number']

    def __str__(self):
        return f"{self.name} (Route: {self.route.name})"

class Vehicle(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    route = models.ForeignKey(Route, related_name='vehicles', on_delete=models.CASCADE)
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    heading = models.FloatField(default=0)  # Direction in degrees
    speed = models.FloatField(default=0)  # Current speed in mph
    next_stop = models.ForeignKey(Stop, null=True, blank=True, on_delete=models.SET_NULL)
    estimated_arrival = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.identifier} on {self.route.name}"

class TravelHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    passengers_boarding = models.IntegerField(default=0)
    passengers_alighting = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Travel histories"

    def __str__(self):
        return f"{self.vehicle.identifier} at {self.stop.name}"
