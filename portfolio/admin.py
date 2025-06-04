from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import path
from django import forms
from .models import Education, Certification, Project, ProjectImage, ProjectVideo, ProjectDocument, Contact, Profile, Message, Publication, WorkExperience, WorkExperienceImage, WorkExperienceDocument

def copy_spanish_to_english(modeladmin, request, queryset):
    for obj in queryset:
        for field in obj._meta.fields:
            field_name = field.name
            if field_name.endswith('_en'):
                continue
                
            field_en_name = f"{field_name}_en"
            if hasattr(obj, field_en_name):
                value = getattr(obj, field_name)
                setattr(obj, field_en_name, value)
        obj.save()
    modeladmin.message_user(request, f"Contenido en español copiado al inglés para {queryset.count()} elementos.")
copy_spanish_to_english.short_description = "Copiar español a inglés para los elementos seleccionados"

def copy_english_to_spanish(modeladmin, request, queryset):
    for obj in queryset:
        for field in obj._meta.fields:
            field_name = field.name
            if not field_name.endswith('_en'):
                continue
                
            field_es_name = field_name[:-3]
            if hasattr(obj, field_es_name):
                value = getattr(obj, field_name)
                if value:
                    setattr(obj, field_es_name, value)
        obj.save()
    modeladmin.message_user(request, f"Contenido en inglés copiado al español para {queryset.count()} elementos.")
copy_english_to_spanish.short_description = "Copiar inglés a español para los elementos seleccionados"

class BilingualAdmin(admin.ModelAdmin):
    change_form_template = 'admin/bilingual_change_form.html'
    actions = [copy_spanish_to_english, copy_english_to_spanish]
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<path:object_id>/copy-es-to-en/',
                self.admin_site.admin_view(self.copy_es_to_en),
                name=f'{self.model._meta.app_label}_{self.model._meta.model_name}_copy_es_to_en',
            ),
            path(
                '<path:object_id>/copy-en-to-es/',
                self.admin_site.admin_view(self.copy_en_to_es),
                name=f'{self.model._meta.app_label}_{self.model._meta.model_name}_copy_en_to_es',
            ),
        ]
        return custom_urls + urls
    
    def copy_es_to_en(self, request, object_id):
        obj = self.get_object(request, object_id)
        
        # Obtener todos los campos con versión en inglés
        for field in obj._meta.fields:
            field_name = field.name
            if field_name.endswith('_en'):
                # Ignorar si ya es un campo en inglés
                continue
                
            # Verificar si existe el campo correspondiente en inglés
            field_en_name = f"{field_name}_en"
            if hasattr(obj, field_en_name):
                # Copiar el valor del campo en español al campo en inglés
                value = getattr(obj, field_name)
                setattr(obj, field_en_name, value)
        
        obj.save()
        self.message_user(request, "Contenido en español copiado al inglés correctamente.")
        return HttpResponseRedirect("../")
    
    def copy_en_to_es(self, request, object_id):
        obj = self.get_object(request, object_id)
        
        # Obtener todos los campos con versión en inglés
        for field in obj._meta.fields:
            field_name = field.name
            if not field_name.endswith('_en'):
                # Ignorar si no es un campo en inglés
                continue
                
            # Obtener el nombre del campo en español
            field_es_name = field_name[:-3]  # Quitar el sufijo '_en'
            if hasattr(obj, field_es_name):
                # Copiar el valor del campo en inglés al campo en español
                value = getattr(obj, field_name)
                if value:  # Solo copiar si hay contenido
                    setattr(obj, field_es_name, value)
        
        obj.save()
        self.message_user(request, "Contenido en inglés copiado al español correctamente.")
        return HttpResponseRedirect("../")

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fieldsets = (
        ('Español', {
            'fields': ('image', 'caption', 'order')
        }),
        ('English', {
            'fields': ('caption_en',),
        }),
    )

class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1
    fieldsets = (
        ('Español', {
            'fields': ('video', 'caption', 'order')
        }),
        ('English', {
            'fields': ('caption_en',),
        }),
    )

class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1
    fieldsets = (
        ('Español', {
            'fields': ('document', 'title', 'order')
        }),
        ('English', {
            'fields': ('title_en',),
        }),
    )

class WorkExperienceImageInline(admin.TabularInline):
    model = WorkExperienceImage
    extra = 1

class WorkExperienceDocumentInline(admin.TabularInline):
    model = WorkExperienceDocument
    extra = 1

class ProjectAdminForm(forms.ModelForm):
    SKILL_CHOICES = [
        ('data_scientist', 'Data Scientist'),
        ('data_analyst', 'Data Analyst'),
        ('python_developer', 'Python Developer'),
    ]
    
    skill_choices = forms.MultipleChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Habilidades"
    )
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.skills:
            # Si es una edición, establecer los valores iniciales
            self.initial['skill_choices'] = [skill.strip() for skill in self.instance.skills.split(',')]
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Guardar las habilidades seleccionadas como una cadena separada por comas
        if self.cleaned_data.get('skill_choices'):
            instance.skills = ','.join(self.cleaned_data['skill_choices'])
        else:
            instance.skills = ''
        if commit:
            instance.save()
        return instance

@admin.register(Education)
class EducationAdmin(BilingualAdmin):
    list_display = ('institution', 'title', 'graduation_year', 'is_active', 'order', 'has_english_content')
    list_filter = ('is_active',)
    search_fields = ('institution', 'title')
    list_editable = ('is_active', 'order')
    fieldsets = (
        ('Español', {
            'fields': ('institution', 'title', 'description')
        }),
        ('English', {
            'fields': ('institution_en', 'title_en', 'description_en'),
        }),
        ('Información Común', {
            'fields': ('graduation_year', 'is_active', 'order'),
        }),
    )
    
    def has_english_content(self, obj):
        return bool(obj.title_en and obj.institution_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"

@admin.register(Certification)
class CertificationAdmin(BilingualAdmin):
    list_display = ('name', 'institution', 'date_obtained', 'is_valid', 'is_active', 'order', 'has_english_content')
    list_filter = ('is_active',)
    search_fields = ('name', 'institution')
    list_editable = ('is_active', 'order')
    fieldsets = (
        ('Español', {
            'fields': ('name', 'institution', 'description')
        }),
        ('English', {
            'fields': ('name_en', 'institution_en', 'description_en'),
        }),
        ('Información Común', {
            'fields': ('date_obtained', 'expiry_date', 'certificate_file', 'credential_url', 'is_active', 'order'),
        }),
    )
    
    def has_english_content(self, obj):
        return bool(obj.name_en and obj.institution_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"

@admin.register(Project)
class ProjectAdmin(BilingualAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'get_type_display', 'skills', 'technologies', 'is_active', 'order', 'has_english_content')
    list_filter = ('is_active', 'type')
    search_fields = ('title', 'description', 'technologies', 'skills')
    list_editable = ('is_active', 'order')
    inlines = [ProjectImageInline, ProjectVideoInline, ProjectDocumentInline]
    
    def get_type_display(self, obj):
        return obj.get_type_display()
    get_type_display.short_description = "Tipo"
    
    def get_fieldsets(self, request, obj=None):
        common_fields = ('type', 'skill_choices')
        project_fields = ('project_url', 'github_url')
        
        fieldsets = [
            ('Español', {
                'fields': ('title', 'description', 'technologies')
            }),
            ('English', {
                'fields': ('title_en', 'description_en', 'technologies_en'),
            }),
            ('Tipo de entrada', {
                'fields': common_fields,
                'description': 'Seleccione el tipo y sus habilidades'
            }),
            ('Campos de proyecto', {
                'fields': project_fields,
                'description': 'URLs del proyecto'
            }),
            ('Información Común', {
                'fields': ('thumbnail', 'is_active', 'order'),
            }),
        ]
        return fieldsets
    
    def has_english_content(self, obj):
        return bool(obj.title_en and obj.description_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'is_active', 'order')
    list_filter = ('type', 'is_active')
    search_fields = ('value',)
    list_editable = ('is_active', 'order')

@admin.register(Profile)
class ProfileAdmin(BilingualAdmin):
    list_display = ('name', 'title', 'has_english_content')
    fieldsets = (
        ('Español', {
            'fields': ('name', 'title', 'bio')
        }),
        ('English', {
            'fields': ('name_en', 'title_en', 'bio_en'),
        }),
        ('Fotografías', {
            'fields': ('photo', 'professional_photo'),
            'description': 'La foto principal (photo) se muestra en la sección de héroe. La foto profesional aparecerá junto al nombre.'
        }),
    )
    
    def has_english_content(self, obj):
        return bool(obj.name_en and obj.title_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"

@admin.register(Publication)
class PublicationAdmin(BilingualAdmin):
    list_display = ('title', 'get_type_display', 'authors', 'journal_or_publisher', 'publication_date', 'is_active', 'order', 'has_english_content')
    list_filter = ('is_active', 'type', 'publication_date')
    search_fields = ('title', 'authors', 'journal_or_publisher', 'abstract')
    list_editable = ('is_active', 'order')
    date_hierarchy = 'publication_date'
    
    def get_type_display(self, obj):
        return obj.get_type_display()
    get_type_display.short_description = "Tipo de Publicación"
    
    def get_fieldsets(self, request, obj=None):
        common_fields = ('type',)
        book_fields = ('isbn',)
        article_fields = ('doi',)
        
        fieldsets = [
            ('Español', {
                'fields': ('title', 'authors', 'journal_or_publisher', 'abstract')
            }),
            ('English', {
                'fields': ('title_en', 'authors_en', 'journal_or_publisher_en', 'abstract_en'),
            }),
            ('Tipo de publicación', {
                'fields': common_fields,
                'description': 'Seleccione el tipo de publicación'
            }),
            ('Identificadores', {
                'fields': ('doi', 'isbn', 'url'),
                'description': 'DOI para artículos científicos, ISBN para libros'
            }),
            ('Archivos', {
                'fields': ('pdf_file', 'thumbnail'),
                'description': 'PDF de la publicación y una imagen para representarla'
            }),
            ('Información Común', {
                'fields': ('publication_date', 'is_active', 'order'),
            }),
        ]
        return fieldsets
    
    def has_english_content(self, obj):
        return bool(obj.title_en and obj.abstract_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"

@admin.register(WorkExperience)
class WorkExperienceAdmin(BilingualAdmin):
    list_display = ('position', 'company', 'skills', 'start_date', 'end_date', 'current_job', 'is_active', 'order', 'has_english_content')
    list_filter = ('is_active', 'current_job')
    search_fields = ('position', 'company', 'description', 'keywords', 'skills')
    list_editable = ('is_active', 'order')
    inlines = [WorkExperienceImageInline, WorkExperienceDocumentInline]
    
    def has_english_content(self, obj):
        return bool(obj.position_en and obj.company_en and obj.description_en)
    has_english_content.boolean = True
    has_english_content.short_description = "¿Tiene versión en inglés?"
    
    fieldsets = (
        ('Español', {
            'fields': ('position', 'company', 'description', 'keywords')
        }),
        ('English', {
            'fields': ('position_en', 'company_en', 'description_en', 'keywords_en'),
        }),
        ('Periodo', {
            'fields': ('start_date', 'end_date', 'current_job'),
            'description': 'Establezca el periodo laboral'
        }),
        ('Detalles adicionales', {
            'fields': ('company_logo', 'skills'),
            'description': 'Logo y habilidades (separadas por comas, ej: "data_scientist, python_developer")'
        }),
        ('Información Común', {
            'fields': ('thumbnail', 'is_active', 'order'),
        }),
    )

def mark_as_read(modeladmin, request, queryset):
    queryset.update(read=True)
mark_as_read.short_description = "Marcar como leído"

def mark_as_unread(modeladmin, request, queryset):
    queryset.update(read=False)
mark_as_unread.short_description = "Marcar como no leído"

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    actions = [mark_as_read, mark_as_unread]
    
    def is_read(self, obj):
        return obj.read
    is_read.boolean = True
    is_read.short_description = "Leído"
    
    def has_add_permission(self, request):
        return False  # No permitir añadir mensajes manualmente
