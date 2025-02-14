import factory
from .models import Heroes
from faker import Faker

fake = Faker()

class HeroesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Heroes

    name = factory.LazyAttribute(lambda x: fake.name())
    perfil = factory.django.ImageField()
    counter = factory.SubFactory('self')
