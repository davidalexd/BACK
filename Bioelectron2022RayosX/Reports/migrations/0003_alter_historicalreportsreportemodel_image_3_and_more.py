# Generated by Django 4.1.5 on 2023-01-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_alter_historicalreportsreportemodel_fecha_control_calidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreportsreportemodel',
            name='image_3',
            field=models.TextField(blank='', default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reportsreportemodel',
            name='image_3',
            field=models.ImageField(blank='', default='', null=True, upload_to='reports/'),
        ),
    ]
