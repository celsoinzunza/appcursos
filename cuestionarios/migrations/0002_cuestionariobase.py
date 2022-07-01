# Generated by Django 4.0.5 on 2022-06-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuestionarioBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Pregunta1', models.CharField(blank=True, choices=[('Exelente', 'Excelente'), ('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=20, null=True, verbose_name='En general como calificarias el curso')),
                ('Pregunta2', models.CharField(blank=True, choices=[('Exelente', 'Excelente'), ('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=20, null=True, verbose_name='En general como calificarias al instructor')),
                ('Pregunta3', models.CharField(blank=True, choices=[('Exelente', 'Excelente'), ('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=20, null=True, verbose_name='En general como calificarias el salon')),
                ('Pregunta4', models.CharField(blank=True, choices=[('si', 'SI'), ('no', 'NO')], max_length=20, null=True, verbose_name='Recomendarias este curso a otras personas')),
                ('Pregunta5', models.CharField(blank=True, max_length=400, null=True, verbose_name='Dinos tus comentarios o recomendaciones para mejorar este curso')),
            ],
            options={
                'verbose_name': 'Cuestionario Base',
                'verbose_name_plural': 'Cuestionario Base',
                'db_table': 'cursos_cuestionarios_base',
            },
        ),
    ]
