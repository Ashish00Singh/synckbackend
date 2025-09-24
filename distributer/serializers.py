
from rest_framework import serializers
from .models import distributer

class distributorSelizer(serializers.ModelSerializer):
    class Meta:
        model = distributer
        fields = "__all__"

    def validate_terms_accepted(self, value):
        if not value:
            raise serializers.ValidationError("⚠️ You must accept the Terms & Conditions before saving.")
        return value
