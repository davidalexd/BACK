# Generated by Django 4.1.1 on 2022-09-27 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '0006_remove_organizacionmodel_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Departamentos_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(editable=False)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.departamentomodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='departamentomodel',
            name='user',
            field=models.ManyToManyField(through='Customer.User_Departamentos_Model', to=settings.AUTH_USER_MODEL),
        ),
    ]
