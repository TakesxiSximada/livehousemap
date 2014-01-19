# Create your views here.
import json
from django.http import HttpResponse
from .models import (
    House,
    Landmark,
    )

def index(request):
    houses = []
    for house in House.objects.all():
        data = {'name': house.name,
                'lat': house.lat,
                'lng': house.lon,
                }
        landmarks = []
        for landmark in Landmark.objects.filter(id=house.id):
            landmark = {'name': landmark.name,
                        'lat': landmark.lat,
                        'lng': landmark.lng,
                        }
            landmarks.append(landmark)
        houses.append(data)
    json_str = json.dumps(houses)
    return HttpResponse(json_str, mimetype='application/json')
