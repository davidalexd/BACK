# Generated by Django 4.1.2 on 2022-10-22 04:57

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Protocol', '0003_remove_historicalprotocolsmodel_protocolo_detalles_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalprotocolsmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical protocols models'},
        ),
        migrations.AlterModelOptions(
            name='historicalpruebacalculomodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical prueba calculo models'},
        ),
        migrations.AlterModelOptions(
            name='historicalpruebaopcionesmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical prueba opciones models'},
        ),
        migrations.AlterModelOptions(
            name='historicalseccionesmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical secciones models'},
        ),
        migrations.AlterField(
            model_name='historicalprotocolsmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpruebacalculomodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpruebaopcionesmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalseccionesmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
