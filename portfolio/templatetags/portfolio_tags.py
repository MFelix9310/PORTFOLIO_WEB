from django import template
from django.utils.translation import get_language

register = template.Library()

@register.filter
def get_translated_field(obj, field_name):
    """
    Retorna el valor del campo en el idioma correcto.
    Si el idioma es inglés, intenta usar el campo con sufijo _en,
    si ese campo no existe o está vacío, usa el campo original (español).
    """
    current_language = get_language() or 'es'
    
    if current_language == 'en':
        en_field = f"{field_name}_en"
        if hasattr(obj, en_field) and getattr(obj, en_field):
            return getattr(obj, en_field)
    
    return getattr(obj, field_name) 