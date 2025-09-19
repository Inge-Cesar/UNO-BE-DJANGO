from django.db import models

class Faculty(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'facultades'
        managed = False

    def __str__(self):
        return self.nombre
