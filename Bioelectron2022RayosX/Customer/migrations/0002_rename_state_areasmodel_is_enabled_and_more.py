# Generated by Django 4.1.1 on 2022-10-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areasmodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='contactosmodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='departamentomodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='historicalareasmodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='historicalcontactosmodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='historicaldepartamentomodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='historicalorganizacionmodel',
            old_name='state',
            new_name='is_enabled',
        ),
        migrations.RenameField(
            model_name='organizacionmodel',
            old_name='state',
            new_name='is_enabled',
        ),
    ]
