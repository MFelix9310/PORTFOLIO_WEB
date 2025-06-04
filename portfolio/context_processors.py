from django.conf import settings

def language_context(request):
    """
    Añade el código de idioma actual al contexto para todas las plantillas.
    """
    lang = request.session.get('django_language', 'es')
    return {
        'LANGUAGE_CODE': lang
    }

def react_enabled(request):
    """
    Adds the REACT_ENABLED setting to the template context.
    This allows templates to know if React is enabled.
    """
    return {'REACT_ENABLED': getattr(settings, 'REACT_ENABLED', False)} 