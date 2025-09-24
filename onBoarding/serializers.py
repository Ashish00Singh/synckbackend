# onbording/serializers.py
from rest_framework import serializers
from .models import Onboarding
from accounts.models import Registerlogin

class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show active users in dropdowns/choices
        self.fields['user'].queryset = Registerlogin.objects.filter(active=True)

    # def validate(self, data):
    #     # Require at least individual or corporate fields
    #     individual_fields = ['name', 'email', 'phone']
    #     corporate_fields = ['company_name', 'gst_number']

    #     has_individual = all(data.get(f) for f in individual_fields)
    #     has_corporate = all(data.get(f) for f in corporate_fields)

    #     if not has_individual and not has_corporate:
    #         raise serializers.ValidationError(
    #             "Either provide all individual fields (name, email, phone) or corporate fields (company_name, gst_number)."
    #         )
    #     return data
