from django.db import models
from infrastructure.models.student_model import Student
from infrastructure.models.materia_model import Materia

class Inscription(models.Model):
    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="inscripciones")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "inscripciones"
        managed = True

    def __str__(self):
        return f"{self.estudiante.nombre} → {self.materia.nombre}"
