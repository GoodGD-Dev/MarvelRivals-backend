from django.urls import path, include
from rest_framework import routers

from heroes import viewsets

router = routers.SimpleRouter()
router.register(r'heroes-list', viewsets.HeroesViewSet, basename='heroes-list')

urlpatterns = [
    path('', include(router.urls)),
]