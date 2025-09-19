from django.db import models

class ProjectState(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        db_table = "estado_proyecto"
        managed = True

    def __str__(self):
        return self.nombre
