# Generated by Django 4.1.5 on 2023-02-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_historicaluser_firma_historicaluser_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='firma',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Imagen de firma'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='image',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Imagen de perfil'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='numero',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firma',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen de firma'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen de perfil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='numero',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
