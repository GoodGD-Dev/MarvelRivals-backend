from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
  list_display = ('name', 'perfil', 'counter')
  search_fields = ('name',)
  autocomplete_fields = ('counter',)