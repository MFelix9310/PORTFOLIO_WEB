from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('education/', views.EducationListView.as_view(), name='education_list'),
    path('certifications/', views.CertificationListView.as_view(), name='certification_list'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('experience/', views.WorkExperienceListView.as_view(), name='work_experience_list'),
    path('experience/<int:pk>/', views.WorkExperienceDetailView.as_view(), name='work_experience_detail'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('publications/', views.PublicationListView.as_view(), name='publication_list'),
    path('contact/', views.contact_view, name='contact'),
    
    # API endpoints for React integration
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/work-experiences/', views.api_work_experiences, name='api_work_experiences'),
] 