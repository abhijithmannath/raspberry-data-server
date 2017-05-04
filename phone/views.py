# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import PiDataSet
from .serializers import DataSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class DataServerView(generics.ListCreateAPIView):
    queryset = PiDataSet.objects.all()
    serializer_class = DataSerializer
    authentication_classes = ( BasicAuthentication,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #POST End Point to UPDATE/CREATE SESSION    
    def post(self, request, *args, **kwargs):
	return self.create(request, *args, **kwargs)
