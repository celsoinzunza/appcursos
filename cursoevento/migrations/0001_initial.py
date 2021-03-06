# Generated by Django 4.0.5 on 2022-07-01 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0003_remove_registroeventos_alumno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('fechayhora_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora de inicio')),
                ('fechayhora_final', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora de finalizacion')),
                ('duracion_hrs', models.IntegerField(blank=True, null=True, verbose_name='Duracion en Horas')),
                ('lugar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Lugar')),
                ('registros_abiertos', models.BooleanField(default=True, verbose_name='Registros Abiertos')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Curso_Evento', to='catalogos.cursos', verbose_name='Curso')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogos.instructor', verbose_name='Instructor')),
            ],
            options={
                'verbose_name': 'Curso Evento',
                'verbose_name_plural': 'Cursos Evento',
                'db_table': 'curso_evento',
            },
        ),
        migrations.CreateModel(
            name='RegistroEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechayhora', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora de inicio')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('pagado', models.BooleanField(default=True, verbose_name='status')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.alumnos', verbose_name='Alumno')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoevento.cursoevento', verbose_name='Curso Evento')),
            ],
            options={
                'verbose_name': 'Registro Evento',
                'verbose_name_plural': 'Registros Eventos',
                'db_table': 'cursos_registroeventos',
            },
        ),
    ]
