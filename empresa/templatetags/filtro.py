from django import template

register = template.Library()

@register.filter(name="par")
def par(valor):
    return True if valor % 2 == 0 else False
