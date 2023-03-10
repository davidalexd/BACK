# Generated by Django 4.1.5 on 2023-02-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_historicaluser_is_staff_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='firma',
            field=models.TextField(max_length=255, null=True, verbose_name='Imagen de firma'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='numero',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='firma',
            field=models.ImageField(max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen de firma'),
        ),
        migrations.AddField(
            model_name='user',
            name='numero',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='image',
            field=models.TextField(max_length=255, null=True, verbose_name='Imagen de perfil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen de perfil'),
        ),
    ]
