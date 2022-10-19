# Generated by Django 4.1.2 on 2022-10-19 17:59

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
            name='Ar_dpt_Model',
            fields=[
                ('id', models.BigAutoField(db_column='ArDpt_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'customers_departamento_ambiente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AreasModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='ar_id', primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(db_column='ar_nombre_area', max_length=255, verbose_name="Area's name")),
                ('ubicacion', models.JSONField(db_column='ar_ubicacion_area', null=True, verbose_name="Area's location")),
            ],
            options={
                'db_table': 'customers_Ambientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Con_Dpt_Model',
            fields=[
                ('id', models.BigAutoField(db_column='ConDpt_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'customers_contactos_departamento',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ContactosModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='con_id', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='con_nombre', default='---', max_length=255, null=True, verbose_name="Contact's name")),
                ('apellidos', models.CharField(blank=True, db_column='con_apellidos', default='---', max_length=255, null=True, verbose_name="Contact's last name")),
                ('dni', models.CharField(blank=True, db_column='con_numero_dni', default='---', max_length=255, null=True, verbose_name="Contact's DNI number")),
                ('numero_telefono', models.CharField(blank=True, db_column='con_numero_telefono', default='---', max_length=255, null=True, verbose_name='Contact phone number')),
                ('correo', models.CharField(blank=True, db_column='con_correo_electronico', default='---', max_length=255, null=True, verbose_name='Contact email address')),
                ('cargo', models.CharField(blank=True, db_column='con_cargo', default='---', max_length=255, null=True, verbose_name='Job')),
            ],
            options={
                'db_table': 'customers_Contactos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DepartamentoModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='dpt_id', primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(db_column='dpt_nombre_departamento', max_length=255, verbose_name="Headquarters's name")),
                ('direccion_departamento', models.CharField(blank=True, db_column='dpt_direccion_departamento', max_length=255, null=True, verbose_name="Headquarters's address")),
                ('pais_departamento', models.CharField(blank=True, db_column='dpt_pais', max_length=255, null=True, verbose_name='Country where the headquarters belongs')),
                ('departamento_departamento', models.CharField(blank=True, db_column='dpt_departamento', max_length=255, null=True, verbose_name='Department to which the headquarters belongs')),
                ('provincia_departamento', models.CharField(blank=True, db_column='dpt_provincia', max_length=255, null=True, verbose_name='Province to which the headquarters belongs')),
                ('distrito_departamento', models.CharField(blank=True, db_column='dpt_distrito', max_length=255, null=True, verbose_name='District to which the headquarters belongs')),
                ('contactos', models.ManyToManyField(through='Customer.Con_Dpt_Model', to='Customer.contactosmodel')),
                ('members', models.ManyToManyField(through='Customer.Ar_dpt_Model', to='Customer.areasmodel')),
            ],
            options={
                'db_table': 'customers_Depatamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dpt_org_Model',
            fields=[
                ('id', models.BigAutoField(db_column='DptOrg_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.departamentomodel')),
            ],
            options={
                'db_table': 'customers_organizacion_departamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrganizacionModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='org_id', primary_key=True, serialize=False)),
                ('ruc', models.CharField(blank=True, db_column='org_ruc', max_length=12, null=True, unique=True, verbose_name="Organization's ruc number")),
                ('razon_social', models.CharField(blank=True, db_column='org_razon_social', max_length=255, unique=True, verbose_name="Organization's name")),
                ('nombre_comercial', models.CharField(blank=True, db_column='org_nombre_comercial', max_length=255, null=True, unique=True, verbose_name="Organization's commercial name ")),
                ('tipo', models.CharField(blank=True, db_column='org_tipo', max_length=255, null=True, verbose_name="Organization's type")),
                ('ciiu', models.IntegerField(blank=True, db_column='org_ciiu', null=True, verbose_name="Organization's International Standard Industrial Classification")),
                ('direccion_legal', models.CharField(blank=True, db_column='org_direccion_legal', max_length=255, null=True, verbose_name="Organization's legal address")),
                ('pais_organizacion', models.CharField(blank=True, db_column='org_pais', max_length=255, null=True, verbose_name='Country where the organization belongs')),
                ('departamento_organizacion', models.CharField(blank=True, db_column='org_departamento', max_length=255, null=True, verbose_name='Department to which the organization belongs')),
                ('provincia_organizacion', models.CharField(blank=True, db_column='org_provincia', max_length=255, null=True, verbose_name='Province to which the organization belongs')),
                ('distrito_organizacion', models.CharField(blank=True, db_column='org_distrito', max_length=255, null=True, verbose_name='District to which the organization belongs')),
                ('members', models.ManyToManyField(through='Customer.Dpt_org_Model', to='Customer.departamentomodel')),
            ],
            options={
                'db_table': 'customers_Organizaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrganizacionModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='org_id', db_index=True)),
                ('ruc', models.CharField(blank=True, db_column='org_ruc', db_index=True, max_length=12, null=True, verbose_name="Organization's ruc number")),
                ('razon_social', models.CharField(blank=True, db_column='org_razon_social', db_index=True, max_length=255, verbose_name="Organization's name")),
                ('nombre_comercial', models.CharField(blank=True, db_column='org_nombre_comercial', db_index=True, max_length=255, null=True, verbose_name="Organization's commercial name ")),
                ('tipo', models.CharField(blank=True, db_column='org_tipo', max_length=255, null=True, verbose_name="Organization's type")),
                ('ciiu', models.IntegerField(blank=True, db_column='org_ciiu', null=True, verbose_name="Organization's International Standard Industrial Classification")),
                ('direccion_legal', models.CharField(blank=True, db_column='org_direccion_legal', max_length=255, null=True, verbose_name="Organization's legal address")),
                ('pais_organizacion', models.CharField(blank=True, db_column='org_pais', max_length=255, null=True, verbose_name='Country where the organization belongs')),
                ('departamento_organizacion', models.CharField(blank=True, db_column='org_departamento', max_length=255, null=True, verbose_name='Department to which the organization belongs')),
                ('provincia_organizacion', models.CharField(blank=True, db_column='org_provincia', max_length=255, null=True, verbose_name='Province to which the organization belongs')),
                ('distrito_organizacion', models.CharField(blank=True, db_column='org_distrito', max_length=255, null=True, verbose_name='District to which the organization belongs')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDepartamentoModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='dpt_id', db_index=True)),
                ('nombre_departamento', models.CharField(db_column='dpt_nombre_departamento', max_length=255, verbose_name="Headquarters's name")),
                ('direccion_departamento', models.CharField(blank=True, db_column='dpt_direccion_departamento', max_length=255, null=True, verbose_name="Headquarters's address")),
                ('pais_departamento', models.CharField(blank=True, db_column='dpt_pais', max_length=255, null=True, verbose_name='Country where the headquarters belongs')),
                ('departamento_departamento', models.CharField(blank=True, db_column='dpt_departamento', max_length=255, null=True, verbose_name='Department to which the headquarters belongs')),
                ('provincia_departamento', models.CharField(blank=True, db_column='dpt_provincia', max_length=255, null=True, verbose_name='Province to which the headquarters belongs')),
                ('distrito_departamento', models.CharField(blank=True, db_column='dpt_distrito', max_length=255, null=True, verbose_name='District to which the headquarters belongs')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContactosModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='con_id', db_index=True)),
                ('nombre', models.CharField(blank=True, db_column='con_nombre', default='---', max_length=255, null=True, verbose_name="Contact's name")),
                ('apellidos', models.CharField(blank=True, db_column='con_apellidos', default='---', max_length=255, null=True, verbose_name="Contact's last name")),
                ('dni', models.CharField(blank=True, db_column='con_numero_dni', default='---', max_length=255, null=True, verbose_name="Contact's DNI number")),
                ('numero_telefono', models.CharField(blank=True, db_column='con_numero_telefono', default='---', max_length=255, null=True, verbose_name='Contact phone number')),
                ('correo', models.CharField(blank=True, db_column='con_correo_electronico', default='---', max_length=255, null=True, verbose_name='Contact email address')),
                ('cargo', models.CharField(blank=True, db_column='con_cargo', default='---', max_length=255, null=True, verbose_name='Job')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAreasModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='ar_id', db_index=True)),
                ('nombre_area', models.CharField(db_column='ar_nombre_area', max_length=255, verbose_name="Area's name")),
                ('ubicacion', models.JSONField(db_column='ar_ubicacion_area', null=True, verbose_name="Area's location")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='dpt_org_model',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.organizacionmodel'),
        ),
        migrations.AddField(
            model_name='con_dpt_model',
            name='contacto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.contactosmodel'),
        ),
        migrations.AddField(
            model_name='con_dpt_model',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.departamentomodel'),
        ),
        migrations.AddField(
            model_name='ar_dpt_model',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.areasmodel'),
        ),
        migrations.AddField(
            model_name='ar_dpt_model',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.departamentomodel'),
        ),
    ]
