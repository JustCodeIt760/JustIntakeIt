from django.urls import path
from . import views

app_name = 'project_initiation'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('wizard/', views.project_wizard, name='project_wizard'),
    path('wizard/<str:step>/', views.project_wizard, name='project_wizard'),
    path('wizard/<str:step>/<int:project_id>/', views.project_wizard, name='project_wizard'),
]