# Generated by Django 3.2.6 on 2022-09-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolsModel',
            fields=[
                ('id', models.BigAutoField(db_column='prt_id', primary_key=True, serialize=False)),
                ('protocolo_titulo', models.CharField(db_column='prt_nombre', max_length=255, unique=True, verbose_name='Protocol name')),
                ('protocolo_detalles', models.JSONField(blank=True, db_column='prt_detalles', null=True, verbose_name='Protocol details')),
                ('is_enabled', models.BooleanField(default=True)),
                ('crated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'protocols_Protocolos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Prt_Scc_Model',
            fields=[
                ('id', models.BigAutoField(db_column='PrtScc_id', primary_key=True, serialize=False)),
                ('crated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'protocols_protocolo_secciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Scc_Prb_Model',
            fields=[
                ('id', models.BigAutoField(db_column='SccPrb_id', primary_key=True, serialize=False)),
                ('crated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'protocols_secciones_prueba',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SeccionesModel',
            fields=[
                ('id', models.BigAutoField(db_column='scc_id', primary_key=True, serialize=False)),
                ('secciones_titulo', models.CharField(db_column='scc_nombre', max_length=255, unique=True, verbose_name='Section name')),
                ('secciones_contexto', models.TextField(blank=True, db_column='scc_contexto', null=True, verbose_name='Section context')),
                ('is_enabled', models.BooleanField(default=True)),
                ('crated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'protocols_Secciones',
                'ordering': ['id'],
            },
        ),
    ]
