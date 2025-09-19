from django.db import models
from infrastructure.models.career_model import Career

class Materia(models.Model):
    carrera = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="materias")
    codigo = models.CharField(max_length=20, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField(null=True, blank=True)
    semestre_materia = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "materias"
        managed = True
        
    def __str__(self):
        return self.nombre
