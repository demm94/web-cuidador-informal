# Generated by Django 3.0.5 on 2020-11-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20201108_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalletema',
            name='nombre',
        ),
        migrations.AddField(
            model_name='detalletema',
            name='descripcion',
            field=models.TextField(default='Agrega una descripción', verbose_name='Descripción'),
        ),
    ]
