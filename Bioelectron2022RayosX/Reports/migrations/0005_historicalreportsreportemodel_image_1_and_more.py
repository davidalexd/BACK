# Generated by Django 4.1.3 on 2022-12-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0004_alter_historicalreportsreportemodel_componente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreportsreportemodel',
            name='image_1',
            field=models.TextField(blank='', default='', max_length=100),
        ),
        migrations.AddField(
            model_name='historicalreportsreportemodel',
            name='image_2',
            field=models.TextField(blank='', default='', max_length=100),
        ),
        migrations.AddField(
            model_name='historicalreportsreportemodel',
            name='image_3',
            field=models.TextField(blank='', default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reportsreportemodel',
            name='image_1',
            field=models.ImageField(blank='', default='', upload_to='reports/'),
        ),
        migrations.AddField(
            model_name='reportsreportemodel',
            name='image_2',
            field=models.ImageField(blank='', default='', upload_to='reports/'),
        ),
        migrations.AddField(
            model_name='reportsreportemodel',
            name='image_3',
            field=models.ImageField(blank='', default='', upload_to='reports/'),
        ),
    ]
