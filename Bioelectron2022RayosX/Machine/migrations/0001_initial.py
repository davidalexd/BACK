# Generated by Django 4.1.2 on 2022-10-16 19:39

import User.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='stm_id', primary_key=True, serialize=False)),
                ('marca', models.CharField(db_column='stm_marca_sistema', max_length=255, verbose_name='System brand')),
                ('modelo', models.CharField(db_column='stm_modelo_sistema', max_length=255, verbose_name='System model')),
                ('serie', models.CharField(db_column='stm_serie_sistema', max_length=255, unique=True, verbose_name='System series')),
                ('antiguedad', models.DateField(blank=True, db_column='stm_antiguedad_sistema', null=True, verbose_name="System's year")),
                ('year_instalacion', models.DateField(blank=True, db_column='stm_year_sistema', null=True, verbose_name="System's nstallation")),
            ],
            options={
                'db_table': 'machines_Sistemas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TuboModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='tb_id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='tb_title_componente', max_length=255, verbose_name='Component brand')),
                ('marca', models.CharField(db_column='tb_marca_componente', max_length=255, verbose_name='Component brand')),
                ('modelo', models.CharField(db_column='tb_modelo_componente', max_length=255, verbose_name='Component model')),
                ('serie', models.CharField(db_column='tb_serie_componente', max_length=255, unique=True, verbose_name='Component series')),
                ('antiguedad', models.DateField(blank=True, db_column='tb_antiguedad_tcomponente', null=True, verbose_name="Component's year")),
                ('year_instalacion', models.DateField(db_column='tb_year_componente', null=True, verbose_name="Component's installation")),
            ],
            options={
                'db_table': 'machines_Tubos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Stm_Tb_Model',
            fields=[
                ('id', models.BigAutoField(db_column='StmTb_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine.sistemamodel')),
                ('tubo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine.tubomodel')),
            ],
            options={
                'db_table': 'reports_sistemas_tubos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sistemamodel',
            name='members',
            field=models.ManyToManyField(through='Machine.Stm_Tb_Model', to='Machine.tubomodel'),
        ),
        migrations.CreateModel(
            name='HistoricalTuboModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='tb_id', db_index=True)),
                ('title', models.CharField(db_column='tb_title_componente', max_length=255, verbose_name='Component brand')),
                ('marca', models.CharField(db_column='tb_marca_componente', max_length=255, verbose_name='Component brand')),
                ('modelo', models.CharField(db_column='tb_modelo_componente', max_length=255, verbose_name='Component model')),
                ('serie', models.CharField(db_column='tb_serie_componente', db_index=True, max_length=255, verbose_name='Component series')),
                ('antiguedad', models.DateField(blank=True, db_column='tb_antiguedad_tcomponente', null=True, verbose_name="Component's year")),
                ('year_instalacion', models.DateField(db_column='tb_year_componente', null=True, verbose_name="Component's installation")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'verbose_name_plural': 'historical tubo models',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSistemaModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='stm_id', db_index=True)),
                ('marca', models.CharField(db_column='stm_marca_sistema', max_length=255, verbose_name='System brand')),
                ('modelo', models.CharField(db_column='stm_modelo_sistema', max_length=255, verbose_name='System model')),
                ('serie', models.CharField(db_column='stm_serie_sistema', db_index=True, max_length=255, verbose_name='System series')),
                ('antiguedad', models.DateField(blank=True, db_column='stm_antiguedad_sistema', null=True, verbose_name="System's year")),
                ('year_instalacion', models.DateField(blank=True, db_column='stm_year_sistema', null=True, verbose_name="System's nstallation")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'verbose_name_plural': 'historical sistema models',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
