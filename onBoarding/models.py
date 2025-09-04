from django.db import models
from accounts.models import Registerlogin

class Onboarding(models.Model):
    user = models.ForeignKey(Registerlogin, on_delete=models.CASCADE)
    
    # Individual fields
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    # Corporate specific fields
    company_name = models.CharField(max_length=200, blank=True, null=True)
    createds = models.DateTimeField(auto_now_add=True)
    gst_numbers = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        # Show name if available, else company_name
        return f"{self.name or self.company_name}"
