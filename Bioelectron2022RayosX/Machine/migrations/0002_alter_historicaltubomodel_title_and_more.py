# Generated by Django 4.1.2 on 2022-10-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltubomodel',
            name='title',
            field=models.CharField(db_column='tb_title_componente', max_length=255, verbose_name='Component title'),
        ),
        migrations.AlterField(
            model_name='tubomodel',
            name='title',
            field=models.CharField(db_column='tb_title_componente', max_length=255, verbose_name='Component title'),
        ),
    ]
