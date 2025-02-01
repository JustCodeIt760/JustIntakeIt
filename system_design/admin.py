from django.contrib import admin
from .models import (
    AWSComponent,
    APIEndpoint,
    UIComponent,
    SystemIntegration,
    ArchitectureDiagram
)

@admin.register(AWSComponent)
class AWSComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'component_type', 'status', 'estimated_cost', 'created_by')
    list_filter = ('component_type', 'status', 'created_date')
    search_fields = ('name', 'description')
    filter_horizontal = ('dependencies',)

@admin.register(APIEndpoint)
class APIEndpointAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'aws_component', 'created_by')
    list_filter = ('method', 'aws_component', 'created_date')
    search_fields = ('path', 'description')

@admin.register(UIComponent)
class UIComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'component_type', 'status', 'created_by')
    list_filter = ('component_type', 'status', 'created_date')
    search_fields = ('name', 'description')

@admin.register(SystemIntegration)
class SystemIntegrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'integration_type', 'provider', 'status', 'created_by')
    list_filter = ('integration_type', 'status', 'created_date')
    search_fields = ('name', 'description', 'provider')
    filter_horizontal = ('aws_components',)

@admin.register(ArchitectureDiagram)
class ArchitectureDiagramAdmin(admin.ModelAdmin):
    list_display = ('title', 'diagram_type', 'version', 'created_by')
    list_filter = ('diagram_type', 'created_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('aws_components',)