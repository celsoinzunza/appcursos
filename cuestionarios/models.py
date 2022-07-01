from django.db import models


SINO_OPTIONS = [
    ('si', 'SI'),
    ('no', 'NO'),
]

REGULAR_OPTIONS = [
    ('Exelente', 'Excelente'),
    ('Bueno', 'Bueno'),
    ('Regular', 'Regular'),
    ('Malo', 'Malo'),
]
# Create your models here.
class Cuestionarios(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = 'cursos_cuestionarios'
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class CuestionariosPreguntas(models.Model):
    cuestionario = models.ForeignKey(Cuestionarios, verbose_name="Cuestionario", on_delete=models.CASCADE, null=True, blank=True)
    pregunta = models.CharField(max_length=200, verbose_name="Pregunta")
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = 'cursos_cuestionarios_preguntas'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __unicode__(self):
        return self.pregunta

    def __str__(self):
        return self.pregunta


class CuestionariosRespuestas(models.Model):
    pregunta = models.ForeignKey(CuestionariosPreguntas, verbose_name="Pregunta", on_delete=models.CASCADE, null=True, blank=True)
    respuesta = models.CharField(max_length=200, verbose_name="Respuesta")

    class Meta:
        db_table = 'cursos_cuestionarios_respuestas'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

class CuestionarioBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    Pregunta1 = models.CharField(verbose_name="En general como calificarias el curso", choices=REGULAR_OPTIONS, max_length=20,null=True, blank=True)
    Pregunta2 = models.CharField(verbose_name="En general como calificarias al instructor", choices=REGULAR_OPTIONS, max_length=20,null=True, blank=True)
    Pregunta3 = models.CharField(verbose_name="En general como calificarias el salon", choices=REGULAR_OPTIONS, max_length=20,null=True, blank=True)
    Pregunta4 = models.CharField(verbose_name="Recomendarias este curso a otras personas", choices=SINO_OPTIONS, max_length=20,null=True, blank=True)
    Pregunta5 = models.CharField(verbose_name="Dinos tus comentarios o recomendaciones para mejorar este curso", max_length=400, null=True, blank=True)

    class Meta:
        db_table = 'cursos_cuestionarios_base'
        verbose_name = 'Cuestionario Base'
        verbose_name_plural = 'Cuestionario Base'