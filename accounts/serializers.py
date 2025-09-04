from rest_framework import serializers
from accounts.models import Registerlogin


class RegisterSerilizer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Registerlogin
        fields='__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)



class ProfileSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Registerlogin
        fields='__all__'