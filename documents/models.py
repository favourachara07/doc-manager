# Define the structure of the data.
# Applying migrations in Django serves several important purposes:

# 1. Database Schema Management
# Migrations are used to manage changes to the database schema over time. They allow you to:

# Create Tables: When you define new models, migrations create the corresponding tables in the database.
# Alter Tables: When you modify existing models (e.g., adding or removing fields), migrations apply these changes to the database schema.
# Delete Tables: When you delete models, migrations remove the corresponding tables from the database.
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.title