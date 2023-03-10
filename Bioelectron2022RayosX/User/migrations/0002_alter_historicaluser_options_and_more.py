# Generated by Django 4.1.2 on 2022-10-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Usuario', 'verbose_name_plural': 'historical Usuarios'},
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
