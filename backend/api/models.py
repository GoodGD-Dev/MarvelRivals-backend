from django.db import models
import uuid

class Hero(models.Model):
  name = models.CharField(max_length=50)
  perfil = models.ImageField(upload_to='hero/', null=True, blank=True)
  counter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='contadores')

  def __str__(self):
    return self.name