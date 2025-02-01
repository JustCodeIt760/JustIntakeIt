from django.urls import path
from . import views

app_name = 'system_design'

urlpatterns = [
    path('', views.system_design_dashboard, name='dashboard'),
    path('aws-components/', views.aws_component_list, name='aws_components'),
    path('api-endpoints/', views.api_endpoint_list, name='api_endpoints'),
    path('ui-components/', views.ui_component_list, name='ui_components'),
    path('integrations/', views.integration_list, name='integrations'),
    path('diagrams/', views.architecture_diagram_list, name='diagrams'),
]