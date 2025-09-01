from rest_framework import serializers
from accounts.models import Registerlogin

class loginSerilizer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Registerlogin
        fields='__all__'