from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Education, Certification, Project, Contact, Profile, Message, Publication, WorkExperience
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# Mixin para incluir el perfil en todas las vistas
class ProfileContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['profile'] = Profile.objects.first()
        except Profile.DoesNotExist:
            context['profile'] = None
        context['contact_list'] = Contact.objects.filter(is_active=True)
        return context

# Create your views here.
class HomeView(ProfileContextMixin, TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education_list'] = Education.objects.filter(is_active=True)[:3]
        context['certification_list'] = Certification.objects.filter(is_active=True)[:3]
        context['project_list'] = Project.objects.filter(is_active=True)[:3]
        context['work_list'] = WorkExperience.objects.filter(is_active=True)[:3]
        context['publication_list'] = Publication.objects.filter(is_active=True)[:3]  # Mostrar solo las 3 últimas publicaciones
        return context
        
class EducationListView(ProfileContextMixin, ListView):
    model = Education
    template_name = 'portfolio/education_list.html'
    context_object_name = 'education_list'
    
    def get_queryset(self):
        return Education.objects.filter(is_active=True)

class CertificationListView(ProfileContextMixin, ListView):
    model = Certification
    template_name = 'portfolio/certification_list.html'
    context_object_name = 'certification_list'
    
    def get_queryset(self):
        return Certification.objects.filter(is_active=True)

class ProjectListView(ProfileContextMixin, ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'project_list'
    
    def get_queryset(self):
        return Project.objects.filter(is_active=True, type='project').order_by('order', '-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkExperienceListView(ProfileContextMixin, ListView):
    model = WorkExperience
    template_name = 'portfolio/work_experience_list.html'
    context_object_name = 'work_list'
    
    def get_queryset(self):
        return WorkExperience.objects.filter(is_active=True).order_by('order', '-start_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkExperienceDetailView(ProfileContextMixin, DetailView):
    model = WorkExperience
    template_name = 'portfolio/work_experience_detail.html'
    context_object_name = 'work'
    
    def get_queryset(self):
        return WorkExperience.objects.filter(is_active=True)

class ProjectDetailView(ProfileContextMixin, DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.filter(is_active=True)

class PublicationListView(ProfileContextMixin, ListView):
    model = Publication
    template_name = 'portfolio/publication_list.html'
    context_object_name = 'publication_list'
    
    def get_queryset(self):
        return Publication.objects.filter(is_active=True).order_by('-publication_date')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')
        
        # Guardar el mensaje en la base de datos
        new_message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )
        new_message.save()
        
        email_message = f"Name: {name}\nEmail: {email}\n\n{message_text}"
        
        try:
            send_mail(
                subject=f"Portfolio Contact: {subject}",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Enviar al email del administrador
            )
            messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
            return redirect('portfolio:contact')
        except Exception as e:
            messages.error(request, f"Hubo un error al enviar tu mensaje: {str(e)}")
    
    context = {
        'contact_list': Contact.objects.filter(is_active=True),
        'profile': Profile.objects.first()
    }
    return render(request, 'portfolio/contact.html', context)

@require_GET
def api_projects(request):
    """API endpoint to provide project data for React components"""
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
    
    projects_data = []
    for project in projects:
        project_data = {
            'id': project.id,
            'title': project.title,
            'title_en': project.title_en,
            'description': project.description,
            'description_en': project.description_en,
            'technologies': project.technologies,
            'technologies_en': project.technologies_en,
            'thumbnail': project.thumbnail.url if project.thumbnail else None,
            'skills': project.skills,
            'github_url': project.github_url,
            'project_url': project.project_url,
            'type': project.type,
        }
        projects_data.append(project_data)
    
    return JsonResponse({'projects': projects_data})

@require_GET
def api_work_experiences(request):
    """API endpoint to provide work experience data for React components"""
    work_experiences = WorkExperience.objects.filter(is_active=True).order_by('order', '-start_date')
    
    work_data = []
    for work in work_experiences:
        work_item = {
            'id': work.id,
            'company': work.company,
            'company_en': work.company_en,
            'position': work.position,
            'position_en': work.position_en,
            'description': work.description,
            'description_en': work.description_en,
            'start_date': work.start_date.strftime('%Y-%m-%d'),
            'end_date': work.end_date.strftime('%Y-%m-%d') if work.end_date else None,
            'current_job': work.current_job,
            'thumbnail': work.thumbnail.url if work.thumbnail else None,
            'company_logo': work.company_logo.url if work.company_logo else None,
            'skills': work.skills,
            'keywords': work.keywords,
            'keywords_en': work.keywords_en,
        }
        work_data.append(work_item)
    
    return JsonResponse({'work_experiences': work_data})
