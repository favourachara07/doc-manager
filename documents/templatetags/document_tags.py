# documents/templatetags/document_tags.py
#Ensure the templatetags directory has an __init__.py file to make it a Python package.
from django import template

register = template.Library()

@register.filter
def is_txt_file(file_name):
    return file_name.endswith('.txt')