from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

people=[
    {
        'First':'Henok',
        'Last': 'Tadesse',
        'Handle':'@henoktad'
    },
    {
        'First':'Teme',
        'Last': 'Meta',
        'Handle':'@tememeta'
    },
    {
        'First':'Kaleb',
        'Last': 'chala',
        'Handle':'@KalebCha'
    }
]




def say_hello(request):
   
    ctx={
     'people':people
    }
    return render(request,'sensor_data_temp.html',ctx)