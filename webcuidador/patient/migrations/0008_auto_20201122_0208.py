# Generated by Django 3.0.5 on 2020-11-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20201108_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)')], default='Soltero', max_length=10, verbose_name='Estado Civil'),
        ),
    ]
