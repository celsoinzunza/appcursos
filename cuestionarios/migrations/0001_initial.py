# Generated by Django 4.0.5 on 2022-06-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Cuestionario',
                'verbose_name_plural': 'Cuestionarios',
                'db_table': 'cursos_cuestionarios',
            },
        ),
        migrations.CreateModel(
            name='CuestionariosPreguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200, verbose_name='Pregunta')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('cuestionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuestionarios.cuestionarios', verbose_name='Cuestionario')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
                'db_table': 'cursos_cuestionarios_preguntas',
            },
        ),
        migrations.CreateModel(
            name='CuestionariosRespuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=200, verbose_name='Respuesta')),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuestionarios.cuestionariospreguntas', verbose_name='Pregunta')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
                'db_table': 'cursos_cuestionarios_respuestas',
            },
        ),
    ]
