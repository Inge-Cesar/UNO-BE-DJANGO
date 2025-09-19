from django.db import models
from infrastructure.models.project_model import Proyecto
from infrastructure.models.student_model import Student

class ProyectoMiembro(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="miembros")
    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, null=True, blank=True)
    es_lider = models.BooleanField(default=False)

    class Meta:
        db_table = "proyectos_miembros"
        managed = True

    def __str__(self):
        return f"{self.estudiante.nombre} → {self.proyecto.titulo}"
