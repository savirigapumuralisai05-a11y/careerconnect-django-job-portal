from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="add_class")
def add_class(field, css_class):
    return mark_safe(str(field).replace('class="', f'class="{conditional_escape(css_class)} ', 1)
                     if 'class="' in str(field)
                     else str(field).replace("<input", f'<input class="{conditional_escape(css_class)}"', 1)
                          .replace("<select", f'<select class="{conditional_escape(css_class)}"', 1)
                          .replace("<textarea", f'<textarea class="{conditional_escape(css_class)}"', 1))
