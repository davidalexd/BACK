# Generated by Django 4.1.2 on 2022-10-22 15:32

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyMachine', '0002_alter_historicalcalibracionesmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcalibracionesmodel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User},
        ),
        migrations.AlterModelOptions(
            name='historicalmedidoresmodel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User},
        ),
        migrations.AlterField(
            model_name='historicalcalibracionesmodel',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalmedidoresmodel',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]
