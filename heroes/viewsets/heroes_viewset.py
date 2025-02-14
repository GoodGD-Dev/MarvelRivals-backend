from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from heroes.models import Heroes
from heroes.serializers import HeroesSerializer

class HeroesViewSet(ModelViewSet):
  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
  permission_classes = [IsAuthenticated]
  serializer_class = HeroesSerializer
  queryset = Heroes.objects.all()