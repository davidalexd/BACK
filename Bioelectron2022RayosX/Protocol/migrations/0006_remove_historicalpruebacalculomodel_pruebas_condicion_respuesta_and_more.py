# Generated by Django 4.1.2 on 2022-10-23 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Protocol', '0005_remove_historicalpruebacalculomodel_pruebas_resultado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpruebacalculomodel',
            name='pruebas_condicion_respuesta',
        ),
        migrations.RemoveField(
            model_name='pruebacalculomodel',
            name='pruebas_condicion_respuesta',
        ),
    ]
