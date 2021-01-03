# Generated by Django 3.0.5 on 2020-12-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20201218_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestanpi',
            name='evaluacion',
            field=models.CharField(default=None, max_length=50, verbose_name='Evaluación'),
        ),
        migrations.AddField(
            model_name='respuestanpi',
            name='resultado',
            field=models.IntegerField(default=None, verbose_name='Resultado'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)')], default='Soltero', max_length=10, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r10b',
            field=models.IntegerField(blank=True, null=True, verbose_name='10b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r11b',
            field=models.IntegerField(blank=True, null=True, verbose_name='11b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r12b',
            field=models.IntegerField(blank=True, null=True, verbose_name='12b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r1b',
            field=models.IntegerField(blank=True, null=True, verbose_name='1b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r2b',
            field=models.IntegerField(blank=True, null=True, verbose_name='2b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r3b',
            field=models.IntegerField(blank=True, null=True, verbose_name='3b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r4b',
            field=models.IntegerField(blank=True, null=True, verbose_name='4b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r5b',
            field=models.IntegerField(blank=True, null=True, verbose_name='5b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r6b',
            field=models.IntegerField(blank=True, null=True, verbose_name='6b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r7b',
            field=models.IntegerField(blank=True, null=True, verbose_name='7b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r8b',
            field=models.IntegerField(blank=True, null=True, verbose_name='8b'),
        ),
        migrations.AlterField(
            model_name='respuestanpi',
            name='r9b',
            field=models.IntegerField(blank=True, null=True, verbose_name='9b'),
        ),
    ]
