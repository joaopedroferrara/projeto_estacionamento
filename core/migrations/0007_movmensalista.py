# Generated by Django 3.2.19 on 2023-05-04 00:50

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_mensalista_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pagto', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mensalista', models.ForeignKey(on_delete=core.models.Mensalista, to='core.mensalista')),
            ],
        ),
    ]
