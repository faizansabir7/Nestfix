from django import template

register = template.Library()

@register.filter
def to_five(value):
    return range(value, 5)
