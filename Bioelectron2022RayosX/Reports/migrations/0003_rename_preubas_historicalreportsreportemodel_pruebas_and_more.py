# Generated by Django 4.1.2 on 2022-10-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_historicalreportsreportemodel_preubas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalreportsreportemodel',
            old_name='preubas',
            new_name='pruebas',
        ),
        migrations.RenameField(
            model_name='reportsreportemodel',
            old_name='preubas',
            new_name='pruebas',
        ),
        migrations.AlterField(
            model_name='historicalreportsreportemodel',
            name='fecha_control_calidad',
            field=models.DateField(blank=True, db_column='rpt_fecha_control_calidad', editable=False, verbose_name='QC date'),
        ),
        migrations.AlterField(
            model_name='reportsreportemodel',
            name='fecha_control_calidad',
            field=models.DateField(auto_now_add=True, db_column='rpt_fecha_control_calidad', verbose_name='QC date'),
        ),
    ]
