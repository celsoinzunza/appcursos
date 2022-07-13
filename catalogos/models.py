from django.db import models
import os
from core.utils import get_filename
from core.validators import validate_file_extension


# Create your models here.
def get_image(instance, filename):
    name, ext = os.path.splitext(filename)

    return "instructores/%s" % get_filename(ext)


class Categorias(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=150, unique=True)
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos_categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Cursos(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=150, unique=True)
    description = models.CharField(
        verbose_name="Descripcion", max_length=800, null=True, blank=True
    )
    description2 = models.CharField(
        verbose_name="Descripcion 2", max_length=800, null=True, blank=True
    )
    description3 = models.CharField(
        verbose_name="Descripcion 3", max_length=800, null=True, blank=True
    )
    categoria = models.ForeignKey(
        Categorias,
        verbose_name="Categoria",
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
        blank=True,
    )
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos"
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Instructor(models.Model):
    first_name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellido", max_length=200)
    telefono = models.CharField(verbose_name="Telefono", max_length=200)
    email = models.CharField(verbose_name="e-Mail", max_length=200)
    picture = models.ImageField(
        upload_to=get_image,
        validators=[validate_file_extension],
        verbose_name="Imagen",
        null=True,
        blank=True,
    )
    rfc = models.CharField(verbose_name="RFC", max_length=14,null=True, blank=True)
    banco = models.CharField(verbose_name="Banco", max_length=50, null=True, blank=True)
    cuentabancaria = models.CharField(verbose_name="Cuenta Bancaria", max_length=100, null=True, blank=True)
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "Instructor"
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    @property
    def picture_url(self):
        if self.picture and hasattr(self.picture, "url"):
            return self.picture.url

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Empresa(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    rfc = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    address = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    city = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    state = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    country = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    cp = models.CharField(verbose_name="Nombre", max_length=200, blank=True, null=True)
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos_empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class AlumnoSelfRegister(models.Model):
    first_name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellido", max_length=200)
    email = models.CharField(verbose_name="email", max_length=200)
    phone = models.CharField(verbose_name="Telefono", max_length=200)
    empresa = models.CharField(verbose_name="Empresa", max_length=200)
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos_alumnos_self"
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name


class Alumnos(models.Model):
    first_name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellido", max_length=200)
    email = models.CharField(verbose_name="email", max_length=200)
    phone = models.CharField(verbose_name="Telefono", max_length=200)
    empresa = models.ForeignKey(
        Empresa, verbose_name="Empresa", on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.BooleanField(verbose_name="status", default=True)

    class Meta:
        db_table = "cursos_alumnos"
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

class Sedes(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la sede")
    domicilio = models.CharField(max_length=50, verbose_name="Domicilio",  null=True, blank=True)
    Estado = models.CharField(max_length=50, verbose_name="Estado",  null=True, blank=True)
    Ciudad = models.CharField(max_length=50, verbose_name="Ciudad", null=True, blank=True)
    cp = models.CharField(max_length=50, verbose_name="Codigo postal", null=True, blank=True)
    telefono = models.CharField(max_length=50, verbose_name="Telefono",  null=True, blank=True)
    rfc = models.CharField(max_length=50, verbose_name="RFC",  null=True, blank=True)
    banco = models.CharField(max_length=50, verbose_name="Banco",  null=True, blank=True)
    cuentabancaria = models.CharField(max_length=50, verbose_name="Cuenta Bancaria",  null=True, blank=True)
    nombrecontacto = models.CharField(max_length=50, verbose_name="Nombre contacto",  null=True, blank=True)
    capacidad = models.IntegerField(verbose_name="Capacidad", null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "cursos_sedes"
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name