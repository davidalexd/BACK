# Generated by Django 4.1.1 on 2022-10-02 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaModel',
            fields=[
                ('id', models.BigAutoField(db_column='stm_id', primary_key=True, serialize=False)),
                ('marca', models.CharField(db_column='stm_marca_sistema', max_length=255, verbose_name='System brand')),
                ('modelo', models.CharField(db_column='stm_modelo_sistema', max_length=255, verbose_name='System model')),
                ('serie', models.CharField(db_column='stm_serie_sistema', max_length=255, unique=True, verbose_name='System series')),
                ('antiguedad', models.DateField(blank=True, db_column='stm_antiguedad_sistema', null=True, verbose_name="System's year")),
                ('year_instalacion', models.DateField(blank=True, db_column='stm_year_sistema', null=True, verbose_name="System's nstallation")),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'machines_Sistemas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TuboModel',
            fields=[
                ('id', models.BigAutoField(db_column='tb_id', primary_key=True, serialize=False)),
                ('marca', models.CharField(db_column='tb_marca_tubo', max_length=255, verbose_name='Tube brand')),
                ('modelo', models.CharField(db_column='tb_modelo_tubo', max_length=255, verbose_name='Tube model')),
                ('serie', models.CharField(db_column='tb_serie_tubo', max_length=255, unique=True, verbose_name='Tube series')),
                ('antiguedad', models.DateField(blank=True, db_column='tb_antiguedad_tubo', null=True, verbose_name="Tube's year")),
                ('year_instalacion', models.DateField(db_column='tb_year_tubo', null=True, verbose_name="Tube's installation")),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'machines_Tubos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User_tubos_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(blank=True, editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine.tubomodel')),
                ('model_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_sistemas_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(blank=True, editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine.sistemamodel')),
                ('model_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tubomodel',
            name='users',
            field=models.ManyToManyField(through='Machine.User_tubos_Model', to=settings.AUTH_USER_MODEL),
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
        migrations.AddField(
            model_name='sistemamodel',
            name='users',
            field=models.ManyToManyField(through='Machine.User_sistemas_Model', to=settings.AUTH_USER_MODEL),
        ),
    ]
