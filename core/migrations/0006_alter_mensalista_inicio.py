# Generated by Django 3.2.19 on 2023-05-04 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='inicio',
            field=models.DateField(),
        ),
    ]
