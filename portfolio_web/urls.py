"""
URL configuration for portfolio_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

# Vista para cambiar idioma
def set_language_view(request):
    """
    Vista para cambiar el idioma de la sesión.
    """
    lang = request.GET.get('lang', 'es')
    next_url = request.GET.get('next', '/')
    
    response = HttpResponseRedirect(next_url)
    response.set_cookie('django_language', lang)
    
    # Guardar el idioma en la sesión también
    request.session['django_language'] = lang
    
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),
    path('', RedirectView.as_view(url='portfolio/', permanent=True)),
    path('set-language/', set_language_view, name='set_language'),
]

# Añadir soporte para archivos media en entorno de desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
