# Generated by Django 3.0.5 on 2020-12-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20201224_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestanpi',
            name='evaluacion',
        ),
        migrations.RemoveField(
            model_name='respuestanpi',
            name='resultado',
        ),
        migrations.AddField(
            model_name='respuestazarit',
            name='evaluacion',
            field=models.CharField(default=None, max_length=50, verbose_name='Evaluación'),
        ),
        migrations.AddField(
            model_name='respuestazarit',
            name='resultado',
            field=models.IntegerField(default=None, verbose_name='Resultado'),
        ),
    ]
