# Generated by Django 4.1.5 on 2023-01-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0003_alter_historicalreportsreportemodel_image_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreportsreportemodel',
            name='image_3',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reportsreportemodel',
            name='image_3',
            field=models.ImageField(null=True, upload_to='reports/'),
        ),
    ]
