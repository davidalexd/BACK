# Generated by Django 4.1.2 on 2022-10-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsistemamodel',
            name='antiguedad',
            field=models.DateField(db_column='stm_antiguedad_sistema', null=True, verbose_name="System's year"),
        ),
        migrations.AlterField(
            model_name='historicalsistemamodel',
            name='year_instalacion',
            field=models.DateField(db_column='stm_year_sistema', null=True, verbose_name="System's nstallation"),
        ),
        migrations.AlterField(
            model_name='sistemamodel',
            name='antiguedad',
            field=models.DateField(db_column='stm_antiguedad_sistema', null=True, verbose_name="System's year"),
        ),
        migrations.AlterField(
            model_name='sistemamodel',
            name='year_instalacion',
            field=models.DateField(db_column='stm_year_sistema', null=True, verbose_name="System's nstallation"),
        ),
    ]
