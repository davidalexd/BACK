# Generated by Django 4.1.2 on 2022-10-22 04:57

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalareasmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical areas models'},
        ),
        migrations.AlterModelOptions(
            name='historicalcontactosmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical contactos models'},
        ),
        migrations.AlterModelOptions(
            name='historicaldepartamentomodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical departamento models'},
        ),
        migrations.AlterModelOptions(
            name='historicalorganizacionmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical organizacion models'},
        ),
        migrations.AlterField(
            model_name='historicalareasmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalcontactosmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaldepartamentomodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalorganizacionmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]