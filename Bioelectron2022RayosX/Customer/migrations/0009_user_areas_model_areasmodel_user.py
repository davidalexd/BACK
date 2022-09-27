# Generated by Django 4.1.1 on 2022-09-27 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customer', '0008_rename_departamento_user_departamentos_model_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Areas_Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('context', models.TextField()),
                ('registerd_at', models.DateTimeField(editable=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.areasmodel')),
                ('model_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='areasmodel',
            name='user',
            field=models.ManyToManyField(through='Customer.User_Areas_Model', to=settings.AUTH_USER_MODEL),
        ),
    ]
