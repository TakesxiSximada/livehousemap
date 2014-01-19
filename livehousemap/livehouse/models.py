from django.db.models import Model
from django.db.models.fields import (
    CharField,
    FloatField,
    )

# Create your models here.
class House(Model):
    name = CharField(max_length=1024)
    lat = FloatField()
    lon = FloatField()

    
class Landmark(Model):
    name = CharField(max_length=1024)
    lat = FloatField()
    lon = FloatField()

