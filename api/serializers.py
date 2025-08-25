from rest_framework import serializers
from api.models import SynckPlan


# create serializers

class SynckHealthPlan(serializers.ModelSerializer):
    class Meta:
        model=SynckPlan
        fields="__all__"
