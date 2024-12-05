# URLs: Map URLs to views.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('delete/<int:document_id>/', views.delete_document, name='delete_document'),
]