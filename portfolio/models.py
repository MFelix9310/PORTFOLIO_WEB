from django.db import models
from django.utils import timezone

class Education(models.Model):
    # Campos en español
    institution = models.CharField(max_length=255, verbose_name="Institución")
    title = models.CharField(max_length=255, verbose_name="Título")
    graduation_year = models.IntegerField(verbose_name="Año de graduación")
    description = models.TextField(blank=True, verbose_name="Descripción")
    
    # Campos en inglés
    institution_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Institution (English)")
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (English)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Description (English)")
    
    # Campos comunes
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order', '-graduation_year']
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.title} - {self.institution}"

class Certification(models.Model):
    # Campos en español
    name = models.CharField(max_length=255, verbose_name="Nombre")
    institution = models.CharField(max_length=255, verbose_name="Institución")
    description = models.TextField(blank=True, verbose_name="Descripción")
    
    # Campos en inglés
    name_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name (English)")
    institution_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Institution (English)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Description (English)")
    
    # Campos comunes
    date_obtained = models.DateField(verbose_name="Fecha de obtención")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Fecha de expiración")
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True, verbose_name="Archivo de certificado")
    credential_url = models.URLField(blank=True, null=True, verbose_name="URL de la credencial")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order', '-date_obtained']
        verbose_name_plural = 'Certifications'
    
    def __str__(self):
        return f"{self.name} - {self.institution}"
    
    @property
    def is_valid(self):
        if not self.expiry_date:
            return True
        return self.expiry_date >= timezone.now().date()

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre (English)")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    # Campos en español
    company = models.CharField(max_length=255, verbose_name="Empresa")
    position = models.CharField(max_length=255, verbose_name="Cargo")
    description = models.TextField(verbose_name="Descripción")
    
    # Campos en inglés
    company_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company (English)")
    position_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Position (English)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Description (English)")
    
    # Campos comunes
    company_logo = models.ImageField(upload_to='companies/', blank=True, null=True, verbose_name="Logo de la empresa")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de fin")
    current_job = models.BooleanField(default=False, verbose_name="Trabajo actual")
    skills = models.CharField(max_length=255, blank=True, null=True, verbose_name="Habilidades (separadas por comas)")
    keywords = models.CharField(max_length=255, blank=True, default="", verbose_name="Palabras clave/Funciones desempeñadas")
    keywords_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Keywords/Functions (English)")
    thumbnail = models.ImageField(upload_to='work/', verbose_name="Imagen miniatura")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"
    
    def __str__(self):
        return f"{self.position} - {self.company}"
        
    def get_skills_list(self):
        if not self.skills:
            return []
        return [skill.strip() for skill in self.skills.split(',')]

class Project(models.Model):
    PROJECT_TYPES = [
        ('project', 'Proyecto'),
    ]
    
    SKILLS = [
        ('data_scientist', 'Data Scientist'),
        ('data_analyst', 'Data Analyst'),
        ('python_developer', 'Python Developer'),
    ]
    
    # Campos comunes
    type = models.CharField(max_length=10, choices=PROJECT_TYPES, default='project', verbose_name="Tipo")
    skills = models.CharField(max_length=255, blank=True, null=True, verbose_name="Habilidades", help_text="Selecciona las habilidades en el formulario de edición")
    
    # Campos en español
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    technologies = models.CharField(max_length=255, verbose_name="Tecnologías")
    
    # Campos en inglés
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (English)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Description (English)")
    technologies_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Technologies (English)")
    
    # Campos comunes
    project_url = models.URLField(blank=True, null=True, verbose_name="URL del proyecto")
    github_url = models.URLField(blank=True, null=True, verbose_name="URL de GitHub")
    thumbnail = models.ImageField(upload_to='projects/', verbose_name="Imagen miniatura")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
        
    def get_skills_list(self):
        if not self.skills:
            return []
        return [skill.strip() for skill in self.skills.split(',')]

class Publication(models.Model):
    PUBLICATION_TYPES = [
        ('book', 'Libro'),
        ('article', 'Artículo Científico'),
        ('conference', 'Conferencia'),
        ('thesis', 'Tesis'),
        ('other', 'Otro'),
    ]
    
    # Campos comunes
    type = models.CharField(max_length=15, choices=PUBLICATION_TYPES, default='article', verbose_name="Tipo de Publicación")
    
    # Campos en español
    title = models.CharField(max_length=255, verbose_name="Título")
    authors = models.CharField(max_length=255, verbose_name="Autores")
    journal_or_publisher = models.CharField(max_length=255, verbose_name="Revista/Editorial")
    abstract = models.TextField(verbose_name="Resumen")
    
    # Campos en inglés
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (English)")
    authors_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Authors (English)")
    journal_or_publisher_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Journal/Publisher (English)")
    abstract_en = models.TextField(blank=True, null=True, verbose_name="Abstract (English)")
    
    # Campos comunes
    publication_date = models.DateField(verbose_name="Fecha de publicación")
    doi = models.CharField(max_length=100, blank=True, null=True, verbose_name="DOI")
    isbn = models.CharField(max_length=20, blank=True, null=True, verbose_name="ISBN")
    url = models.URLField(blank=True, null=True, verbose_name="URL de la publicación")
    pdf_file = models.FileField(upload_to='publications/', blank=True, null=True, verbose_name="Archivo PDF")
    thumbnail = models.ImageField(upload_to='publications/', blank=True, null=True, verbose_name="Imagen de portada")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        ordering = ['order', '-publication_date']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
    
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, verbose_name="Proyecto")
    image = models.ImageField(upload_to='projects/images/', verbose_name="Imagen")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Pie de foto")
    caption_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caption (English)")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Image for {self.project.title}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, related_name='videos', on_delete=models.CASCADE, verbose_name="Proyecto")
    video = models.FileField(upload_to='projects/videos/', verbose_name="Video")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Pie de video")
    caption_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caption (English)")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Video for {self.project.title}"

class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, related_name='documents', on_delete=models.CASCADE, verbose_name="Proyecto")
    document = models.FileField(upload_to='projects/documents/', verbose_name="Documento")
    title = models.CharField(max_length=255, verbose_name="Título")
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (English)")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} for {self.project.title}"

class Contact(models.Model):
    CONTACT_TYPES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
        ('phone', 'Phone'),
        ('email', 'Email'),
    ]
    
    type = models.CharField(max_length=20, choices=CONTACT_TYPES, verbose_name="Tipo")
    value = models.CharField(max_length=255, verbose_name="Valor")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"

class Profile(models.Model):
    # Campos en español
    name = models.CharField(max_length=255, verbose_name="Nombre")
    title = models.CharField(max_length=255, verbose_name="Título profesional")
    bio = models.TextField(verbose_name="Biografía")
    
    # Campos en inglés
    name_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name (English)")
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Professional Title (English)")
    bio_en = models.TextField(blank=True, null=True, verbose_name="Biography (English)")
    
    # Campos comunes
    photo = models.ImageField(upload_to='profile/', verbose_name="Foto principal")
    professional_photo = models.ImageField(upload_to='profile/professional/', blank=True, null=True, help_text="Foto profesional que aparecerá junto al nombre en la sección principal.", verbose_name="Foto profesional")
    
    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Asunto")
    message = models.TextField(verbose_name="Mensaje")
    read = models.BooleanField(default=False, verbose_name="Leído")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
    
    def __str__(self):
        return f"{self.subject} - {self.name} ({self.email})"

class WorkExperienceImage(models.Model):
    work_experience = models.ForeignKey(WorkExperience, related_name='images', on_delete=models.CASCADE, verbose_name="Experiencia Laboral")
    image = models.ImageField(upload_to='work/images/', verbose_name="Imagen")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Pie de foto")
    caption_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caption (English)")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Image for {self.work_experience.position} at {self.work_experience.company}"

class WorkExperienceDocument(models.Model):
    work_experience = models.ForeignKey(WorkExperience, related_name='documents', on_delete=models.CASCADE, verbose_name="Experiencia Laboral")
    document = models.FileField(upload_to='work/documents/', verbose_name="Documento")
    title = models.CharField(max_length=255, verbose_name="Título")
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title (English)")
    order = models.IntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} for {self.work_experience.position} at {self.work_experience.company}"
