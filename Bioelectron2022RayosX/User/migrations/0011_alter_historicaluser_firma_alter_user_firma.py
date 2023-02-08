# Generated by Django 4.1.5 on 2023-02-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_historicaluser_firma_alter_user_firma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='firma',
            field=models.TextField(blank='', default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firma',
            field=models.ImageField(blank='', default='', null=True, upload_to='perfil/'),
        ),
    ]