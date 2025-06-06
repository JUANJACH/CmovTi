from django.contrib.auth.models import User
from django.db import models

class Ticket(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Resuelto', 'Resuelto'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_creados')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='Media')
    creado_en = models.DateTimeField(auto_now_add=True)
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Ticket #{self.id}: {self.titulo}"