# Generated by Django 4.1.2 on 2022-10-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Protocol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprotocolsmodel',
            name='protocolo_detalles',
            field=models.JSONField(db_column='prt_detalles', null=True, verbose_name='Protocol details'),
        ),
        migrations.AddField(
            model_name='protocolsmodel',
            name='protocolo_detalles',
            field=models.JSONField(db_column='prt_detalles', null=True, verbose_name='Protocol details'),
        ),
    ]