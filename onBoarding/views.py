# onBoarding/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Onboarding
from .serializers import OnboardingSerializer

class OnboardingViewSet(viewsets.ModelViewSet):
    queryset = Onboarding.objects.all()
    serializer_class = OnboardingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": "success",
            "status_code":status.HTTP_200_OK,
            "count": queryset.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "status": "success",
            "status_code":status.HTTP_200_OK,
            "data": serializer.data
        }, status=status.HTTP_200_OK)
