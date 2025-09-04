# onbording/views.py
from rest_framework import viewsets
from .models import Onboarding
from .serializers import OnboardingSerializer

class OnboardingViewSet(viewsets.ModelViewSet):
    queryset = Onboarding.objects.all()
    serializer_class = OnboardingSerializer

