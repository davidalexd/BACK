# Generated by Django 4.1.5 on 2023-01-21 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganizacionmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldepartamentomodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcontactosmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalareasmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dpt_org_model',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.departamentomodel'),
        ),
        migrations.AddField(
            model_name='dpt_org_model',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.organizacionmodel'),
        ),
        migrations.AddField(
            model_name='departamentomodel',
            name='contactos',
            field=models.ManyToManyField(through='Customer.Con_Dpt_Model', to='Customer.contactosmodel'),
        ),
        migrations.AddField(
            model_name='departamentomodel',
            name='members',
            field=models.ManyToManyField(through='Customer.Ar_dpt_Model', to='Customer.areasmodel'),
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
