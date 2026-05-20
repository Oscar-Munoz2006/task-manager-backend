from django.db import models

class Task(models.Model):

    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    PRIORITY_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='media')
    deadline = models.DateField(null=True, blank=True)
    deadline_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title