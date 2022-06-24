# Generated by Django 4.0.5 on 2022-06-22 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco_origem', models.CharField(max_length=1000)),
                ('agencia_origem', models.CharField(max_length=100)),
                ('conta_origem', models.CharField(max_length=100)),
                ('banco_destino', models.CharField(max_length=1000)),
                ('agencia_destino', models.CharField(max_length=100)),
                ('conta_destino', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('data_transacao', models.DateTimeField()),
                ('data_upload', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]