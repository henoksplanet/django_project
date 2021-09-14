from django.shortcuts import render
from django.http import HttpResponse
from sensor_data.models import Sensor_Type,sensor_full_data


def say_hello(request):
   
    ctx={
     'sensor_data_obj':sensor_full_data.objects.all()
    }
    return render(request,'sensor_data_temp.html',ctx)