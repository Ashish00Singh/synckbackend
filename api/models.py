from django.db import models

# Create your models here.
# create Plans models 

class SynckPlan(models.Model):
    name = models.CharField(max_length=150)
    domains= models.CharField(max_length=150)
    planId=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    featcher = models.TextField(blank=False, null=False)
    update= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)