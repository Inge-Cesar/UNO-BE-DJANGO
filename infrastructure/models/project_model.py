from django.db import models
from infrastructure.models.student_model import Student
from infrastructure.models.teacher_model import Teacher
from infrastructure.models.project_state_model import ProjectState

class Proyecto(models.Model):
    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="proyectos_creados")
    tutor = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.ForeignKey(ProjectState, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "proyectos"
        managed = True

    def __str__(self):
        return self.titulo
