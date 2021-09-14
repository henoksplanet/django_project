from django.contrib import admin
from .models import sensor_full_data,Sensor_Type
# Register your models here.

admin.site.register(sensor_full_data)
admin.site.register(Sensor_Type)
