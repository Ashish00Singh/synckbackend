from django.shortcuts import render
from rest_framework import viewsets
from addiPlans.models import AdditionalPlan, Covrage
from addiPlans.serializers import Additionalserilizer, Covrageserilizer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class AdditionalViewsSet(viewsets.ModelViewSet):
    queryset=AdditionalPlan.objects.all()
    serializer_class=Additionalserilizer

# AdditionalPlan/pk/CovragePlan
    @action(detail=True, methods=['get'] )
    def CovragePlan(self, request, pk=None):
        try:
            additio=AdditionalPlan.objects.get(pk=pk)
            additionalPlan=AdditionalPlan.objects.values_list("id", flat=True).get(pk=pk)
            cov=Covrage.objects.filter(additional_planId=additionalPlan)
            cov_serilisezer=Covrageserilizer(cov, many=True, context={'request':request})
            return Response({
                "additional_planId": additionalPlan,
                "type": additio.type,
                "covrage": cov_serilisezer.data
            })
        except AdditionalPlan.DoesNotExist:
            return Response({"message": "AdditionalPlan Does not exist"}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': str(e)}, status=500)
         

class CovrageViewsSet(viewsets.ModelViewSet):
    queryset=Covrage.objects.all()
    serializer_class=Covrageserilizer

