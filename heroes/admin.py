from django.contrib import admin
from .models import Heroes

@admin.register(Heroes)
class HeroesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'counter')