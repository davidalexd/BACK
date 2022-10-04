# Generated by Django 4.1.1 on 2022-10-04 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Reportes_Categoria_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(blank=True, editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportscategorymodel')),
                ('model_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Reportes_Formatos_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_Reportes_Reportes_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(blank=True, editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsreportemodel')),
                ('model_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='reportsformatsmodel',
            name='variables',
        ),
        migrations.AlterField(
            model_name='frt_cat_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_ar_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_dpt_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_frt_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_med_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_org_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_prb_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_prt_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_secc_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_stm_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='rpt_tb_model',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.DeleteModel(
            name='Rpt_Var_Model',
        ),
        migrations.AddField(
            model_name='user_reportes_formatos_model',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reports.reportsformatsmodel'),
        ),
        migrations.AddField(
            model_name='user_reportes_formatos_model',
            name='model_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
