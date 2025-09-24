from django.shortcuts import render
from rest_framework import viewsets, status
from api.models import SynckPlan
from api.serializers import SynckHealthPlan
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class SynckHealthViewSet(viewsets.ModelViewSet):
    queryset=SynckPlan.objects.all().order_by('-id')
    serializer_class=SynckHealthPlan


    @action(detail=False, methods=['get'], url_path='activePlan')
    def get_active(self, request, *args, **kwargs):       
        active_plan = SynckPlan.objects.filter(active=True)
        serializer = self.get_serializer(active_plan, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['get'], url_path='activePlan')
    def get_active_detail(self, request, pk=None):
        return Response(
            {"error": "Retrieving by ID is not allowed on this endpoint. Use /synckHealtPlan/<id>/ instead."},
            status=status.HTTP_400_BAD_REQUEST
        )