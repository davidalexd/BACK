# Generated by Django 4.1.1 on 2022-10-11 05:41

import User.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProtocolsModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='prt_id', db_index=True)),
                ('protocolo_titulo', models.CharField(db_column='prt_nombre', db_index=True, max_length=255, verbose_name='Protocol name')),
                ('protocolo_detalles', models.JSONField(db_column='prt_detalles', null=True, verbose_name='Protocol details')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPruebaCalculoModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='prb_cal_id', db_index=True)),
                ('pruebas_titulo', models.CharField(db_column='prb_cal_titulo', db_index=True, max_length=255, verbose_name='Test name')),
                ('pruebas_contexto', models.TextField(blank=True, db_column='prb_cal_contexto', null=True, verbose_name='Test context')),
                ('pruebas_resultado', models.TextField(blank=True, db_column='prb_cal_resultado', null=True, verbose_name='Test results')),
                ('pruebas_tolerancia', models.TextField(db_column='prb_cal_tolerancia', verbose_name="Test's tolerance")),
                ('pruebas_condicion_respuesta', models.JSONField(db_column='prb_cal_condicion_respuesta', verbose_name="Test's condition")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPruebaOpcionesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='prb_opc_id', db_index=True)),
                ('pruebas_titulo', models.CharField(db_column='prb_opc_titulo', db_index=True, max_length=255, verbose_name='Test name')),
                ('pruebas_contexto', models.TextField(blank=True, db_column='prb_opc_contexto', null=True, verbose_name='Test context')),
                ('pruebas_opciones', models.JSONField(db_column='prb_opc_resultado', verbose_name='Test results')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSeccionesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='scc_id', db_index=True)),
                ('secciones_titulo', models.CharField(db_column='scc_nombre', db_index=True, max_length=255, verbose_name='Section name')),
                ('secciones_contexto', models.TextField(blank=True, db_column='scc_contexto', null=True, verbose_name='Section context')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVariablesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('id', models.BigIntegerField(blank=True, db_column='var_id', db_index=True)),
                ('nombre_variable', models.CharField(db_column='var_nombre', max_length=255, verbose_name='Variable name')),
                ('range_variable', models.IntegerField(db_column='var_range', verbose_name='Variable range')),
                ('valor_defecto', models.IntegerField(blank=True, db_column='var_valor_defecto', null=True, verbose_name='Variable valor ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': User.models.User,
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Prb_Calculo_Operacion_Model',
            fields=[
                ('id', models.BigAutoField(db_column='PrbCalOpr_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'tests_calculo_operacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProtocolsModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='prt_id', primary_key=True, serialize=False)),
                ('protocolo_titulo', models.CharField(db_column='prt_nombre', max_length=255, unique=True, verbose_name='Protocol name')),
                ('protocolo_detalles', models.JSONField(db_column='prt_detalles', null=True, verbose_name='Protocol details')),
            ],
            options={
                'db_table': 'protocols_Protocolos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Prueba_Tipo_Model',
            fields=[
                ('id', models.BigAutoField(db_column='PrbCal_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'tests_prueba_tipos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PruebaCalculoModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='prb_cal_id', primary_key=True, serialize=False)),
                ('pruebas_titulo', models.CharField(db_column='prb_cal_titulo', max_length=255, unique=True, verbose_name='Test name')),
                ('pruebas_contexto', models.TextField(blank=True, db_column='prb_cal_contexto', null=True, verbose_name='Test context')),
                ('pruebas_resultado', models.TextField(blank=True, db_column='prb_cal_resultado', null=True, verbose_name='Test results')),
                ('pruebas_tolerancia', models.TextField(db_column='prb_cal_tolerancia', verbose_name="Test's tolerance")),
                ('pruebas_condicion_respuesta', models.JSONField(db_column='prb_cal_condicion_respuesta', verbose_name="Test's condition")),
                ('operacion', models.ManyToManyField(through='Protocol.Prb_Calculo_Operacion_Model', to='Operations.operacionesmodel')),
            ],
            options={
                'db_table': 'tests_PruebaCalculo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PruebaOpcionesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='prb_opc_id', primary_key=True, serialize=False)),
                ('pruebas_titulo', models.CharField(db_column='prb_opc_titulo', max_length=255, unique=True, verbose_name='Test name')),
                ('pruebas_contexto', models.TextField(blank=True, db_column='prb_opc_contexto', null=True, verbose_name='Test context')),
                ('pruebas_opciones', models.JSONField(db_column='prb_opc_resultado', verbose_name='Test results')),
            ],
            options={
                'db_table': 'tests_PruebaOpciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='VariablesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='var_id', primary_key=True, serialize=False)),
                ('nombre_variable', models.CharField(db_column='var_nombre', max_length=255, verbose_name='Variable name')),
                ('range_variable', models.IntegerField(db_column='var_range', verbose_name='Variable range')),
                ('valor_defecto', models.IntegerField(blank=True, db_column='var_valor_defecto', null=True, verbose_name='Variable valor ')),
            ],
            options={
                'db_table': 'protocols_Variables',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SeccionesModel',
            fields=[
                ('is_enabled', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.BigAutoField(db_column='scc_id', primary_key=True, serialize=False)),
                ('secciones_titulo', models.CharField(db_column='scc_nombre', max_length=255, unique=True, verbose_name='Section name')),
                ('secciones_contexto', models.TextField(blank=True, db_column='scc_contexto', null=True, verbose_name='Section context')),
                ('calculo', models.ManyToManyField(through='Protocol.Prueba_Tipo_Model', to='Protocol.pruebacalculomodel')),
                ('opcion', models.ManyToManyField(through='Protocol.Prueba_Tipo_Model', to='Protocol.pruebaopcionesmodel')),
            ],
            options={
                'db_table': 'protocols_Secciones',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='prueba_tipo_model',
            name='calculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocol.pruebacalculomodel'),
        ),
        migrations.AddField(
            model_name='prueba_tipo_model',
            name='opcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocol.pruebaopcionesmodel'),
        ),
        migrations.AddField(
            model_name='prueba_tipo_model',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.seccionesmodel'),
        ),
        migrations.CreateModel(
            name='Prt_Var_Model',
            fields=[
                ('id', models.BigAutoField(db_column='Pr_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.protocolsmodel')),
                ('variables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.variablesmodel')),
            ],
            options={
                'db_table': 'protocols_Protocolo_Variables',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Prt_Scc_Model',
            fields=[
                ('id', models.BigAutoField(db_column='PrtScc_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.protocolsmodel')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.seccionesmodel')),
            ],
            options={
                'db_table': 'protocols_protocolo_secciones',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='protocolsmodel',
            name='secciones',
            field=models.ManyToManyField(through='Protocol.Prt_Scc_Model', to='Protocol.seccionesmodel'),
        ),
        migrations.AddField(
            model_name='protocolsmodel',
            name='variables',
            field=models.ManyToManyField(through='Protocol.Prt_Var_Model', to='Protocol.variablesmodel'),
        ),
        migrations.CreateModel(
            name='Prb_Operacion_Variables',
            fields=[
                ('id', models.BigAutoField(db_column='PrbOprVar_id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.prb_calculo_operacion_model')),
                ('variables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Protocol.variablesmodel')),
            ],
            options={
                'db_table': 'tests_operacion_variables',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='prb_calculo_operacion_model',
            name='calculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocol.pruebacalculomodel'),
        ),
        migrations.AddField(
            model_name='prb_calculo_operacion_model',
            name='operacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Operations.operacionesmodel'),
        ),
        migrations.AddField(
            model_name='prb_calculo_operacion_model',
            name='variable',
            field=models.ManyToManyField(through='Protocol.Prb_Operacion_Variables', to='Protocol.variablesmodel'),
        ),
    ]
