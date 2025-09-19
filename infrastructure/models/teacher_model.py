# infrastructure/models/teacher_model.py
from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    usuario_id = models.BigIntegerField()
    nombre = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    facultad = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "docentes"
        managed = True

    def __str__(self):
        return self.nombre
