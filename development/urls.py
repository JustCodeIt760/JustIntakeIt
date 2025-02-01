from django.urls import path
from . import views

app_name = 'development'

urlpatterns = [
    path('', views.development_dashboard, name='dashboard'),
    path('wizard/', views.development_wizard, name='wizard'),
]