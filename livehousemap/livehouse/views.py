# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('{"houses": [{"lat": 11.111, "lng": 99.999, "name": "testname", "landmarks": []}]}', mimetype='application/json')