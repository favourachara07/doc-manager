# Generated by Django 5.1.3 on 2024-12-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_body_alter_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
