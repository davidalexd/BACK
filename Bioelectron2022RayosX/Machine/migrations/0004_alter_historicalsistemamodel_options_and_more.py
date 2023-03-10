# Generated by Django 4.1.2 on 2022-10-22 04:57

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0003_alter_historicalsistemamodel_antiguedad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalsistemamodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical sistema models'},
        ),
        migrations.AlterModelOptions(
            name='historicaltubomodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical tubo models'},
        ),
        migrations.AlterField(
            model_name='historicalsistemamodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaltubomodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
