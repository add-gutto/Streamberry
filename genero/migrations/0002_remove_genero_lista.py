# Generated by Django 5.1.7 on 2025-07-13 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("genero", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genero",
            name="lista",
        ),
    ]
