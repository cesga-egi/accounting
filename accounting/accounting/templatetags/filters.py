from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def formatTags(value):
    value = value.replace('+', 'and')
    return value.replace(' ', '_')

@register.filter
def get(value, arg):
    try:
        if value.has_key(arg.replace('+', 'and').replace(' ', '_')):
            return value[arg.replace('+', 'and').replace(' ', '_')]
    except:
        pass
    return ""


