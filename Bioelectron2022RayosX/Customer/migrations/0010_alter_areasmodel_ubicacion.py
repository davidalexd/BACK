# Generated by Django 4.1.1 on 2022-09-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0009_user_areas_model_areasmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasmodel',
            name='ubicacion',
            field=models.JSONField(blank=True, db_column='ar_ubicacion_area', null=True, verbose_name="Area's location"),
        ),
    ]
