# Generated by Django 4.1.5 on 2023-01-27 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_sesionesmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sesionesmodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sesionesmodel',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='sesionesmodel',
            name='is_enabled',
        ),
        migrations.RemoveField(
            model_name='sesionesmodel',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='HistoricalSesionesModel',
        ),
    ]
