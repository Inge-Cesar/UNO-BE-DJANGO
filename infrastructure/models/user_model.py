from django.db import models
from .role_model import Role

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    rol = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'usuarios'
        managed = True 

    def __str__(self):
        return self.username
