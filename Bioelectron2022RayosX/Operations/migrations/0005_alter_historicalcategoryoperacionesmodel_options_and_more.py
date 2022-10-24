# Generated by Django 4.1.2 on 2022-10-22 15:32

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0004_alter_historicalcategoryoperacionesmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcategoryoperacionesmodel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User},
        ),
        migrations.AlterModelOptions(
            name='historicaloperacionesmodel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User},
        ),
        migrations.AlterModelOptions(
            name='historicalvariablesmodel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User},
        ),
        migrations.AlterField(
            model_name='historicalcategoryoperacionesmodel',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicaloperacionesmodel',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalvariablesmodel',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]