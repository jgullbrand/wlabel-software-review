from django import template

register = template.Library()

@register.filter
def hyphen_replace(value):
    return value.replace("-"," ")