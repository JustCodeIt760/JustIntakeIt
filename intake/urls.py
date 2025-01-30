from django.urls import path
from . import views

app_name = 'intake'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stakeholders/', views.stakeholder_list, name='stakeholder_list'),
    path('stakeholders/create/', views.stakeholder_create, name='stakeholder_create'),
    path('requirements/', views.requirement_list, name='requirement_list'),
    path('requirements/create/', views.requirement_create, name='requirement_create'),
    path('requirements/<int:pk>/', views.requirement_detail, name='requirement_detail'),
]