# Generated by Django 4.1.1 on 2022-09-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Protocol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variablesmodel',
            name='valor_defecto',
            field=models.IntegerField(blank=True, db_column='var_valor_defecto', null=True, verbose_name='Variable valor '),
        ),
    ]