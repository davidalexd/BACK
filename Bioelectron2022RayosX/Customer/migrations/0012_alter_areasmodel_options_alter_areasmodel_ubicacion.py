# Generated by Django 4.1.1 on 2022-09-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0011_alter_areasmodel_ubicacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areasmodel',
            options={'managed': True, 'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='areasmodel',
            name='ubicacion',
            field=models.JSONField(db_column='ar_ubicacion_area', verbose_name="Area's location"),
        ),
    ]
