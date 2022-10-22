# Generated by Django 4.1.2 on 2022-10-22 04:57

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyMachine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcalibracionesmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical calibraciones models'},
        ),
        migrations.AlterModelOptions(
            name='historicalmedidoresmodel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': User.models.User, 'verbose_name_plural': 'historical medidores models'},
        ),
        migrations.AlterField(
            model_name='historicalcalibracionesmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalmedidoresmodel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
