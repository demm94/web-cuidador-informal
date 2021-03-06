# Generated by Django 3.0.5 on 2020-12-18 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0008_auto_20201122_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre Test')),
            ],
            options={
                'verbose_name': 'Tipo de Test',
                'verbose_name_plural': 'Tipos de Test',
            },
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(choices=[('Casado(a)', 'Casado(a)'), ('Soltero(a)', 'Soltero(a)')], default='Soltero', max_length=10, verbose_name='Estado Civil'),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de realización')),
                ('cuidador', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.TipoTest')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='RespuestaZarit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.IntegerField(verbose_name='r1')),
                ('r2', models.IntegerField(verbose_name='r2')),
                ('r3', models.IntegerField(verbose_name='r3')),
                ('r4', models.IntegerField(verbose_name='r4')),
                ('r5', models.IntegerField(verbose_name='r5')),
                ('r6', models.IntegerField(verbose_name='r6')),
                ('r7', models.IntegerField(verbose_name='r7')),
                ('r8', models.IntegerField(verbose_name='r8')),
                ('r9', models.IntegerField(verbose_name='r9')),
                ('r10', models.IntegerField(verbose_name='r10')),
                ('r11', models.IntegerField(verbose_name='r11')),
                ('r12', models.IntegerField(verbose_name='r12')),
                ('r13', models.IntegerField(verbose_name='r13')),
                ('r14', models.IntegerField(verbose_name='r14')),
                ('r15', models.IntegerField(verbose_name='r15')),
                ('r16', models.IntegerField(verbose_name='r16')),
                ('r17', models.IntegerField(verbose_name='r17')),
                ('r18', models.IntegerField(verbose_name='r18')),
                ('r19', models.IntegerField(verbose_name='r19')),
                ('r20', models.IntegerField(verbose_name='r20')),
                ('r21', models.IntegerField(verbose_name='r21')),
                ('r22', models.IntegerField(verbose_name='r22')),
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.Test')),
            ],
            options={
                'verbose_name': 'Respuesta Zarit',
                'verbose_name_plural': 'Respuestas Zarit',
            },
        ),
        migrations.CreateModel(
            name='RespuestaNPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1a', models.IntegerField(verbose_name='1a')),
                ('r1b', models.IntegerField(verbose_name='1b')),
                ('r2a', models.IntegerField(verbose_name='2a')),
                ('r2b', models.IntegerField(verbose_name='2b')),
                ('r3a', models.IntegerField(verbose_name='3a')),
                ('r3b', models.IntegerField(verbose_name='3b')),
                ('r4a', models.IntegerField(verbose_name='4a')),
                ('r4b', models.IntegerField(verbose_name='4b')),
                ('r5a', models.IntegerField(verbose_name='5a')),
                ('r5b', models.IntegerField(verbose_name='5b')),
                ('r6a', models.IntegerField(verbose_name='6a')),
                ('r6b', models.IntegerField(verbose_name='6b')),
                ('r7a', models.IntegerField(verbose_name='7a')),
                ('r7b', models.IntegerField(verbose_name='7b')),
                ('r8a', models.IntegerField(verbose_name='8a')),
                ('r8b', models.IntegerField(verbose_name='8b')),
                ('r9a', models.IntegerField(verbose_name='9a')),
                ('r9b', models.IntegerField(verbose_name='9b')),
                ('r10a', models.IntegerField(verbose_name='10a')),
                ('r10b', models.IntegerField(verbose_name='10b')),
                ('r11a', models.IntegerField(verbose_name='11a')),
                ('r11b', models.IntegerField(verbose_name='11b')),
                ('r12a', models.IntegerField(verbose_name='12a')),
                ('r12b', models.IntegerField(verbose_name='12b')),
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.Test')),
            ],
            options={
                'verbose_name': 'Respuesta NPI',
                'verbose_name_plural': 'Respuestas NPI',
            },
        ),
    ]
