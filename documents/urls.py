# documents/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('create/', views.create_document, name='create_document'),
    path('delete/<int:document_id>/', views.delete_document, name='delete_document'),
    path('download/<int:document_id>/', views.download_document, name='download_document'),
    path('edit/<int:document_id>/', views.edit_document, name='edit_document'),
]