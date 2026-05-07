from django.db import models

class Comentario(models.Model):
    carta_nombre = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.carta_nombre}: {self.contenido[:20]}"