from rest_framework import serializers
from .models import PiDataSet
#from fields import CustomDateTimeField

#This Serializes and Deserializes Request and Response data for 0 or more sessions

class DataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PiDataSet
	fields = ('temp','humidity','created')
