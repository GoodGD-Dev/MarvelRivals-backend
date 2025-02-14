from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import os
from .models import Heroes

@receiver(post_delete, sender=Heroes)
def delete_hero_image(sender, instance, **kwargs):
    """Deleta a imagem quando o objeto Heroes for deletado."""
    if instance.perfil:
        try:
            # Tenta deletar a imagem
            if os.path.isfile(instance.perfil.path):
                os.remove(instance.perfil.path)
        except (AttributeError, ObjectDoesNotExist):
            # Caso a imagem não exista ou o caminho esteja incorreto
            pass
