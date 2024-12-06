# documents/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from .models import Document
from .forms import DocumentForm, CreateDocumentForm
import os
from django.conf import settings

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            if document.file:
                document.title = document.file.name
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/upload_document.html', {'form': form})

def create_document(request):
    if request.method == 'POST':
        form = CreateDocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            # Create a .txt file with the title and body
            file_path = os.path.join(settings.MEDIA_ROOT, 'documents', f'{document.title}.txt')
            with open(file_path, 'w') as file:
                file.write(document.body)
            document.file.name = f'documents/{document.title}.txt'
            document.save()
            return redirect('document_list')
    else:
        form = CreateDocumentForm()
    return render(request, 'documents/create_document.html', {'form': form})

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.file.delete()  # Delete the file from the filesystem
        document.delete()  # Delete the document record from the database
        return redirect('document_list')
    return render(request, 'documents/confirm_delete.html', {'document': document})

def download_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = os.path.join(settings.MEDIA_ROOT, document.file.name)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response

def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if not document.file.name.endswith('.txt'):
        return redirect('document_list')
    
    if request.method == 'POST':
        form = CreateDocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            file_path = os.path.join(settings.MEDIA_ROOT, document.file.name)
            with open(file_path, 'w') as file:
                file.write(document.body)
            document.save()
            return redirect('document_list')
    else:
        with open(os.path.join(settings.MEDIA_ROOT, document.file.name), 'r') as file:
            document.body = file.read()
        form = CreateDocumentForm(instance=document)
    return render(request, 'documents/edit_document.html', {'form': form, 'document': document})