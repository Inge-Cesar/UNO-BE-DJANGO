from django.db import models

class Role(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'roles'
        managed = True

    def __str__(self):
        return self.nombre
