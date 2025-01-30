from django.contrib import admin
from .models import Stakeholder, RequirementCategory, Requirement

@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'stakeholder_type', 'email', 'influence_level', 'interest_level')
    list_filter = ('stakeholder_type', 'influence_level', 'interest_level')
    search_fields = ('name', 'organization', 'email')
    ordering = ('-influence_level', 'name')

@admin.register(RequirementCategory)
class RequirementCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'description')
    list_filter = ('category_type',)
    search_fields = ('name', 'description')

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'status', 'created_by', 'created_at')
    list_filter = ('category', 'priority', 'status')
    search_fields = ('title', 'description')
    filter_horizontal = ('stakeholders',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('priority', 'status', 'created_at')
