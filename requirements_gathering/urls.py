from django.urls import path
from . import views

app_name = 'requirements_gathering'

urlpatterns = [
    path('', views.requirements_dashboard, name='dashboard'),
    path('surveys/', views.survey_list, name='survey_list'),
    path('operational/', views.operational_requirements_list, name='operational_requirements'),
    path('regulatory/', views.regulatory_compliance_list, name='regulatory_compliance'),
    path('documents/', views.document_list, name='documents'),
    path('interview/', views.quick_interview, name='quick_interview'),
    path('interview/save/', views.save_interview, name='save_interview'),
    path('interview/success/', views.interview_success, name='interview_success'),
    path('interviews/', views.interview_list, name='interview_list'),
]