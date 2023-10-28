from django.shortcuts import render
from django.core.serializers import serialize
from .models import Facility
from django.http import HttpResponse, JsonResponse 
import ast

def home(request):
    return render(request, 'pages/home.html')

def home_map_api(request):
    data = serialize('geojson', Facility.objects.all())
    return HttpResponse(data, content_type='application/json')  

def custom_map_api(request):
    features = {
      'type' : 'FeatureCollection',
      'crs' : {
        'type' : 'name',
        'properties':{
          'name': 'EPSG:4326'
        }
      }    ,
      'features': []
    }
    model = Facility.objects.all()  
    for item in model:
        feature = {
          'geometry': ast.literal_eval(item.location.json),
          'properties': {
            'nama': item.name,
            'tipe': item.types,
            'harga': item.price,
            'satuan_harga': item.price_unit
          }
        }
        features['features'].append(feature)  

    return JsonResponse(features, safe=False)
