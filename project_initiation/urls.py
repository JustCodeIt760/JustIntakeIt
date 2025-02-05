from django.urls import path
from . import views

app_name = 'project_initiation'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('wizard/', views.project_wizard, name='project_wizard'),
    path('wizard/<str:step>/', views.project_wizard, name='project_wizard'),
    path('wizard/<str:step>/<int:project_id>/', views.project_wizard, name='project_wizard'),
    path('stops/<int:stop_id>/', views.stop_detail, name='stop_detail'),
    path('api/stops/<int:stop_id>/status/', views.stop_status, name='stop_status'),
    path('api/stops/<int:stop_id>/next-shuttle-location/', views.next_shuttle_location, name='next_shuttle_location'),
]