# Generated by Django 5.1.7 on 2025-07-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genero", "0002_remove_genero_lista"),
        ("titulo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="titulo",
            name="generos",
            field=models.ManyToManyField(to="genero.genero"),
        ),
    ]
