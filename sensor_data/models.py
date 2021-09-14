from django.db import models
from django.db.models.base import Model
from enum import Enum, unique
class Sensor_Type(models.Model):
    short=models.CharField(max_length=10,primary_key=True)
    long=models.CharField(max_length=30)

class sensor_full_data(models.Model):
    daq= models.IntegerField()
    module_nr=models.IntegerField()
    slot=models.IntegerField()
    ch_nr=models.IntegerField()
    sensor_name=models.CharField(max_length=50)
    serial=models.IntegerField()
    property=models.CharField(max_length=50)
    color_code=models.CharField(max_length=10)
    MP_TP_TW= models.CharField( max_length=3)
    sensor_type=models.ForeignKey(Sensor_Type,on_delete=models.CASCADE)
    tdms_group=models.CharField(max_length=20)
    level_name=models.CharField(max_length=5)
    level_lat_Exact=models.DecimalField(decimal_places=3,max_digits=10)
    level_lat_round_or_name=models.IntegerField()
    heading=models.IntegerField()
    orientation=models.CharField(max_length=2)
    sensor_part_nr=models.IntegerField()
    status=models.IntegerField()


