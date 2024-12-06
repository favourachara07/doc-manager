# Handle user input and file uploads. 
# Form Definition: Created a form for the Document model to handle file uploads.
from django import forms
# Imports the forms module from Django, which provides tools for creating and handling forms.
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'body')