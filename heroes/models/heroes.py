import uuid
from django.db import models

class Heroes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    perfil = models.ImageField(upload_to='heroes/', null=False, blank=False)
    counter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='relacionados')

    def __str__(self):
        return self.name
