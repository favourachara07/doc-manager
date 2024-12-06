# Define the structure of the data.
# Applying migrations in Django serves several important purposes:

#Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema

#makemigrations is responsible for packaging up your model changes into individual migration files - analogous to commits - and migrate is responsible for applying those to your database.

# 1. Database Schema Management
# Migrations are used to manage changes to the database schema(logical blueprint that defines how data is organized and structured within a database) over time. They allow you to:

# Create Tables: When you define new models, migrations create the corresponding tables in the database.
# Alter Tables: When you modify existing models (e.g., adding or removing fields), migrations apply these changes to the database schema.
# Delete Tables: When you delete models, migrations remove the corresponding tables from the database.
# documents/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.title if self.title else self.file.name