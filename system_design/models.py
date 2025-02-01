from django.db import models
from django.contrib.auth.models import User

class AWSComponent(models.Model):
    COMPONENT_TYPES = (
        ('s3', 'Amazon S3'),
        ('lambda', 'AWS Lambda'),
        ('rds', 'Amazon RDS'),
        ('api_gateway', 'API Gateway'),
        ('cognito', 'Amazon Cognito'),
        ('cloudfront', 'CloudFront'),
        ('route53', 'Route 53'),
        ('vpc', 'VPC'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=20, choices=COMPONENT_TYPES)
    description = models.TextField()
    configuration = models.JSONField(help_text="AWS configuration details in JSON format")
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='planned')
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_component_type_display()})"

class APIEndpoint(models.Model):
    HTTP_METHODS = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('PATCH', 'PATCH'),
    )

    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10, choices=HTTP_METHODS)
    description = models.TextField()
    request_schema = models.JSONField(help_text="Expected request format in JSON")
    response_schema = models.JSONField(help_text="Expected response format in JSON")
    aws_component = models.ForeignKey(AWSComponent, on_delete=models.CASCADE, related_name='endpoints')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.method} {self.path}"

class UIComponent(models.Model):
    COMPONENT_TYPES = (
        ('customer_web', 'Customer Web Interface'),
        ('customer_mobile', 'Customer Mobile Interface'),
        ('operator_dashboard', 'Operator Dashboard'),
        ('admin_panel', 'Admin Panel'),
    )

    name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=20, choices=COMPONENT_TYPES)
    description = models.TextField()
    wireframe_url = models.URLField(blank=True, help_text="Link to wireframe/mockup")
    design_file = models.FileField(upload_to='ui_designs/', blank=True)
    features = models.JSONField(help_text="List of features and their descriptions")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='draft')

    def __str__(self):
        return f"{self.name} ({self.get_component_type_display()})"

class SystemIntegration(models.Model):
    INTEGRATION_TYPES = (
        ('payment', 'Payment Gateway'),
        ('gps', 'GPS Tracking'),
        ('notification', 'Notification Service'),
        ('analytics', 'Analytics Service'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=200)
    integration_type = models.CharField(max_length=20, choices=INTEGRATION_TYPES)
    description = models.TextField()
    provider = models.CharField(max_length=100)
    api_documentation = models.URLField(blank=True)
    configuration = models.JSONField(help_text="Integration configuration details")
    aws_components = models.ManyToManyField(AWSComponent, related_name='integrations')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='planned')

    def __str__(self):
        return f"{self.name} ({self.get_integration_type_display()})"

class ArchitectureDiagram(models.Model):
    DIAGRAM_TYPES = (
        ('high_level', 'High Level Architecture'),
        ('detailed', 'Detailed Architecture'),
        ('network', 'Network Diagram'),
        ('data_flow', 'Data Flow Diagram'),
    )

    title = models.CharField(max_length=200)
    diagram_type = models.CharField(max_length=20, choices=DIAGRAM_TYPES)
    description = models.TextField()
    diagram_file = models.FileField(upload_to='architecture_diagrams/')
    version = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    aws_components = models.ManyToManyField(AWSComponent, related_name='diagrams')

    def __str__(self):
        return f"{self.title} v{self.version}"