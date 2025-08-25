from rest_framework import serializers
from addiPlans.models import AdditionalPlan, Covrage


# create serializers

class Additionalserilizer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=AdditionalPlan
        fields="__all__"

class Covrageserilizer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    additionalPlanID = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Covrage
        fields="__all__"
