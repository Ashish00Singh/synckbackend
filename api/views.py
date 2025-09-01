from django.shortcuts import render
from rest_framework import viewsets
from api.models import SynckPlan
from api.serializers import SynckHealthPlan

# Create your views here.

class SynckHealthViewSet(viewsets.ModelViewSet):
    queryset=SynckPlan.objects.all().order_by('-id')
    serializer_class=SynckHealthPlan