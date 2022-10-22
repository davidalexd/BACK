# Generated by Django 4.1.2 on 2022-10-22 04:57

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0005_rpt_prt_model_protocolo_detalles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalreportscategorymodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical reports category models'},
        ),
        migrations.AlterModelOptions(
            name='historicalreportsformatsmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical reports formats models'},
        ),
        migrations.AlterModelOptions(
            name='historicalreportsreportemodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical reports reporte models'},
        ),
        migrations.AlterField(
            model_name='historicalreportscategorymodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalreportsformatsmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalreportsreportemodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]