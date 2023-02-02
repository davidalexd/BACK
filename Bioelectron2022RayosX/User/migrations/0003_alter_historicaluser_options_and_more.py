# Generated by Django 4.1.2 on 2022-10-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_historicaluser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Usuario'},
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]
