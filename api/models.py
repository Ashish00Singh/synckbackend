from django.db import models


class SynckPlan(models.Model):
    name = models.CharField(max_length=150)
    domains= models.CharField(max_length=150)
    planId=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    featcher = models.TextField(blank=False, null=False)
    update= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.planId:
            self.planId = self.planId.upper()   # force uppercase
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.planId}"