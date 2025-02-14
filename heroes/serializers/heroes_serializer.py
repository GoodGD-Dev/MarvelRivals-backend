from rest_framework import serializers
from heroes.models import Heroes

class HeroesSerializer(serializers.ModelSerializer):
    counter = serializers.PrimaryKeyRelatedField(queryset=Heroes.objects.all())

    class Meta:
        model = Heroes
        fields = '__all__'
