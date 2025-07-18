# Generated by Django 5.1.7 on 2025-07-13 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("titulo", "0002_titulo_generos"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_adicionado", models.DateTimeField(auto_now_add=True)),
                (
                    "titulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="titulo.titulo"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("usuario", "titulo")},
            },
        ),
    ]
