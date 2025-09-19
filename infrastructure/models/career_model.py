from django.db import models
from infrastructure.models.faculty_model import Faculty

class Career(models.Model):
    codigo = models.CharField(max_length=20, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    institucion = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "carreras"

    def __str__(self):
        return self.nombre
