# Generated by Django 4.1.2 on 2022-10-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0004_alter_rpt_varr_model_posicion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_prt_model',
            name='protocolo_detalles',
            field=models.JSONField(db_column='RptPrt_detalles', null=True, verbose_name='Protocol details'),
        ),
    ]
