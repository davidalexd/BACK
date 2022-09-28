# Generated by Django 4.1.1 on 2022-09-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0001_initial'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='tubomodel',
            name='antiguedad',
            field=models.DateField(db_column='tb_antiguedad_tubo', null=True, verbose_name="Tube's year"),
        ),
        migrations.AlterField(
            model_name='tubomodel',
            name='year_instalacion',
            field=models.DateField(db_column='tb_year_tubo', null=True, verbose_name="Tube's installation"),
        ),
    ]