from unicodedata import name
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myApp.models import Car

def index(request):
    car = Car.objects.all()
    data = {'result':list(car.values("name","speed"))}
    return JsonResponse(data)

def get_car(request, car_name):
    if request.method == 'GET':
        try:
            #select * from Car where name = car_name
            car = Car.objects.get(name=car_name)
            response = json.dumps([{ 'Car name': car.name, 'Top Speed': car.speed}])
        except:
            response = json.dumps([{ 'Error': 'No car with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        c_name = payload['car_name']
        c_speed = payload['car_speed']
        car = Car(name = c_name , speed = c_speed)
        try:
            car.save()
            response = json.dumps([{'success' : 'car added successfully'}])
        except:
            response = json.dumps([{'error' : 'car could not be added'}])
    return HttpResponse(response, content_type='text/json')