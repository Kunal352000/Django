from django import template
register=template.Library()

def first_two_upper(value):
    "This is my own folder"
    result=value[:2].upper()
    return result

register.filter('first_two_upper',first_two_upper)