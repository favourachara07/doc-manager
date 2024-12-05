from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm
import os
from django.conf import settings

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

def upload_document(request):
    # Checks if the request method is POST, indicating that the form has been submitted.

    if request.method == 'POST':
        # Creates an instance of DocumentForm with the submitted data (request.POST) and files (request.FILES).
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Saves the form data to create a new Document object in the database.
            document = form.save()
            # Save the document to the device
            with open(os.path.join(settings.MEDIA_ROOT, document.file.name), 'wb+') as destination:
                for chunk in document.file.chunks():
                    destination.write(chunk)
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/upload_document.html', {'form': form})

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.file.delete()  # Delete the file from the filesystem
        document.delete()  # Delete the document record from the database
        return redirect('document_list')
    return render(request, 'documents/confirm_delete.html', {'document': document})