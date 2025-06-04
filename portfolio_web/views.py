from django.shortcuts import redirect
from django.http import HttpResponseRedirect

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