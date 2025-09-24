from django.shortcuts import render

from rest_framework import viewsets
from .models import distributer
from .serializers import distributorSelizer

class distributorView(viewsets.ModelViewSet):
    queryset = distributer.objects.all()
    serializer_class = distributorSelizer