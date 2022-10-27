# Generated by Django 4.1.2 on 2022-10-26 23:48

import User.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Protocol', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Operations', '0008_alter_historicalvariablesmodel_nombre_variable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frt_Cat_Model',
            fields=[
                ('id', models.BigAutoField(db_column='FrtCat_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'reports_formatos_categoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ReportsFormatsModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='rep_frt_id', primary_key=True, serialize=False)),
                ('codigo_formato', models.CharField(blank=True, db_column='rep_frt_codigo', max_length=255, null=True, unique=True, verbose_name='Format code')),
                ('nombre_formato', models.CharField(blank=True, db_column='rep_frt_nombre', max_length=255, verbose_name='Format name')),
            ],
            options={
                'db_table': 'reports_Formatos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ReportsReporteModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='rpt_id', primary_key=True, serialize=False)),
                ('nombre_reporte', models.CharField(db_column='rpt_name_reporte', max_length=255, verbose_name='Report name')),
                ('numero_de_ot', models.CharField(db_column='rpt_numero_orden_trabajo', max_length=255, verbose_name='Ot number')),
                ('fecha_control_calidad', models.DateField(db_column='rpt_fecha_control_calidad', verbose_name='QC date')),
                ('observacion', models.TextField(db_column='rpt_observacion_reporte', verbose_name='Report observacion')),
                ('datos_del_cliente', models.JSONField(db_column='rpt_data_clientes', verbose_name='Data for clients')),
                ('sistema', models.JSONField(db_column='rpt_data_sistema', verbose_name='Data for system')),
                ('componente', models.JSONField(db_column='rpt_data_component', verbose_name='Data for component')),
                ('machine', models.JSONField(db_column='rpt_data_maquina', verbose_name='Values for machine')),
                ('valores_operaciones', models.JSONField(db_column='rpt_valores_operaciones', verbose_name='Values for operations')),
            ],
            options={
                'db_table': 'reports_Reportes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rpt_Varr_Model',
            fields=[
                ('id', models.BigAutoField(db_column='RptVar_id', primary_key=True, serialize=False)),
                ('subtitle_posicion', models.TextField(blank=True, db_column='rpt_varr_seccion_title', null=True, verbose_name='Title Seccion')),
                ('posicion', models.IntegerField(db_column='rpt_varr_posicion', verbose_name='Contenedor de Variable en reporte')),
                ('sub_posicion', models.IntegerField(db_column='rpt_varr_sub_posicion', verbose_name='Posicion de variable en contenedor')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('formato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel')),
                ('variable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operations.variablesmodel')),
            ],
            options={
                'db_table': 'reports_formatos_variables',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rpt_Secc_Model',
            fields=[
                ('id', models.BigAutoField(db_column='RptSecc_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('formato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.seccionesmodel')),
            ],
            options={
                'db_table': 'reports_rpt_secc',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rpt_Prt_Model',
            fields=[
                ('id', models.BigAutoField(db_column='RptPrt_id', primary_key=True, serialize=False)),
                ('protocolo_detalles', models.JSONField(db_column='RptPrt_detalles', null=True, verbose_name='Protocol details')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('formato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel')),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.protocolsmodel')),
            ],
            options={
                'db_table': 'reports_rpt_Prt',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rpt_Frt_Model',
            fields=[
                ('id', models.BigAutoField(db_column='RptAr_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('formato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel')),
                ('reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsreportemodel')),
            ],
            options={
                'db_table': 'reports_rpt_Frt',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='reportsreportemodel',
            name='formato',
            field=models.ManyToManyField(through='Reports.Rpt_Frt_Model', to='Reports.reportsformatsmodel'),
        ),
        migrations.AddField(
            model_name='reportsformatsmodel',
            name='protocolo',
            field=models.ManyToManyField(through='Reports.Rpt_Prt_Model', to='Protocol.protocolsmodel'),
        ),
        migrations.AddField(
            model_name='reportsformatsmodel',
            name='secciones',
            field=models.ManyToManyField(through='Reports.Rpt_Secc_Model', to='Protocol.seccionesmodel'),
        ),
        migrations.AddField(
            model_name='reportsformatsmodel',
            name='variables_formato',
            field=models.ManyToManyField(through='Reports.Rpt_Varr_Model', to='Operations.variablesmodel'),
        ),
        migrations.CreateModel(
            name='ReportsCategoryModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='rep_cat_id', primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(db_column='rep_cat_area', max_length=255, verbose_name='Category name')),
                ('abreviatura_categoria', models.CharField(db_column='rep_cat_abreviatura', max_length=255, unique=True, verbose_name='Category abbreviation')),
                ('members', models.ManyToManyField(through='Reports.Frt_Cat_Model', to='Reports.reportsformatsmodel')),
            ],
            options={
                'db_table': 'reports_Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalReportsReporteModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='rpt_id', db_index=True)),
                ('nombre_reporte', models.CharField(db_column='rpt_name_reporte', max_length=255, verbose_name='Report name')),
                ('numero_de_ot', models.CharField(db_column='rpt_numero_orden_trabajo', max_length=255, verbose_name='Ot number')),
                ('fecha_control_calidad', models.DateField(db_column='rpt_fecha_control_calidad', verbose_name='QC date')),
                ('observacion', models.TextField(db_column='rpt_observacion_reporte', verbose_name='Report observacion')),
                ('datos_del_cliente', models.JSONField(db_column='rpt_data_clientes', verbose_name='Data for clients')),
                ('sistema', models.JSONField(db_column='rpt_data_sistema', verbose_name='Data for system')),
                ('componente', models.JSONField(db_column='rpt_data_component', verbose_name='Data for component')),
                ('machine', models.JSONField(db_column='rpt_data_maquina', verbose_name='Values for machine')),
                ('valores_operaciones', models.JSONField(db_column='rpt_valores_operaciones', verbose_name='Values for operations')),
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
            name='HistoricalReportsFormatsModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='rep_frt_id', db_index=True)),
                ('codigo_formato', models.CharField(blank=True, db_column='rep_frt_codigo', db_index=True, max_length=255, null=True, verbose_name='Format code')),
                ('nombre_formato', models.CharField(blank=True, db_column='rep_frt_nombre', max_length=255, verbose_name='Format name')),
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
            name='HistoricalReportsCategoryModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='rep_cat_id', db_index=True)),
                ('nombre_categoria', models.CharField(db_column='rep_cat_area', max_length=255, verbose_name='Category name')),
                ('abreviatura_categoria', models.CharField(db_column='rep_cat_abreviatura', db_index=True, max_length=255, verbose_name='Category abbreviation')),
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
            model_name='frt_cat_model',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportscategorymodel'),
        ),
        migrations.AddField(
            model_name='frt_cat_model',
            name='formatos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel'),
        ),
    ]
