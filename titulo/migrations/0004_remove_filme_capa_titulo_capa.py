# Generated by Django 5.1.7 on 2025-07-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("titulo", "0003_remove_serie_numero_temporadas_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filme",
            name="capa",
        ),
        migrations.AddField(
            model_name="titulo",
            name="capa",
            field=models.ImageField(blank=True, null=True, upload_to="capas/"),
        ),
    ]
