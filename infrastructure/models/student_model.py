from django.db import models
from infrastructure.models.user_model import User
from infrastructure.models.career_model import Career

class Student(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="estudiantes")
    nombre = models.CharField(max_length=150)
    registro = models.CharField(max_length=32, null=True, blank=True)
    carrera = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="estudiantes")
    semestre = models.IntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ppa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "estudiantes"
        managed = True

    def __str__(self):
        return self.nombre
