from django.db import models

from catalogos.models import Cursos, Instructor, Alumnos


# Create your models here.

class CursoEvento(models.Model):
    curso = models.ForeignKey(
        Cursos,
        related_name="Curso_Evento",
        verbose_name="Curso",
        on_delete=models.DO_NOTHING,
    )
    descripcion = models.CharField(verbose_name="Descripcion", max_length=200)
    fechayhora_inicio = models.DateTimeField(
        verbose_name="Fecha y hora de inicio", null=True, blank=True
    )
    fechayhora_final = models.DateTimeField(
        verbose_name="Fecha y hora de finalizacion", null=True, blank=True
    )
    duracion_hrs = models.IntegerField(
        verbose_name="Duracion en Horas", null=True, blank=True
    )
    instructor = models.ForeignKey(
        Instructor,
        verbose_name="Instructor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    lugar = models.CharField(
        verbose_name="Lugar", blank=True, null=True, max_length=200
    )
    registros_abiertos = models.BooleanField(
        verbose_name="Registros Abiertos", default=True
    )
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "curso_evento"
        verbose_name = "Curso Evento"
        verbose_name_plural = "Cursos Evento"

    def __unicode__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion


class RegistroEventos(models.Model):
    evento = models.ForeignKey(
        CursoEvento, verbose_name="Curso Evento", on_delete=models.CASCADE
    )
    alumno = models.ForeignKey(Alumnos, verbose_name="Alumno", on_delete=models.CASCADE)
    fechayhora = models.DateTimeField(
        verbose_name="Fecha y hora de inicio", null=True, blank=True
    )
    status = models.BooleanField(verbose_name="status", default=True)
    pagado = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos_registroeventos"
        verbose_name = "Registro Evento"
        verbose_name_plural = "Registros Eventos"