from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import Registerlogi
from accounts.serializers import loginSerilizer

# Create your views here.
class RegisterloginView(viewsets.ModelViewSet):
    queryset=Registerlogi.objects.all()
    serializer_class=loginSerilizer
