# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PiDataSet(models.Model):
    temp = models.FloatField()
    humidity = models.FloatField()
    data3 = models.FloatField()
    data4 = models.FloatField()
    data5 = models.FloatField()
    data6 = models.FloatField()
    data7 = models.FloatField()
    data8 = models.FloatField()

    
        
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return 'Temp:  %s'%(self.temp)
