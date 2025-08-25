from django.db import models

# Create your models here.

class AdditionalPlan(models.Model):
    type = models.CharField(max_length=50, null=False, blank=False)
    alert= models.TextField(blank=True, null=True)

    class Meta:
        db_table = "AdditionalPlan"

    def __str__(self):
        return self.type

    # coverage=models.ForeignKey(Coverage, on_delete=models.CASCADE)
class Covrage(models.Model):
    # individual=models.PositiveIntegerField(null=True, blank=True)
    # one_adult_one_child=models.PositiveIntegerField(null=True, blank=True)  
    # two_adults=models.PositiveIntegerField(null=True, blank=True) 
    # two_adults_one_child = models.PositiveIntegerField(null=True, blank=True) 
    # two_adults_two_children = models.PositiveIntegerField(null=True, blank=True)

    # two_laks = models.PositiveIntegerField(null=True, blank=True)
    # three_laks = models.PositiveIntegerField(null=True, blank=True)
    # five_laks = models.PositiveIntegerField(null=True, blank=True)
    # seven_laks = models.PositiveIntegerField(null=True, blank=True)
    # ten_laks = models.PositiveIntegerField(null=True, blank=True)
    AGE_BANDS = [
        ("18-35", "18 to 35 Years"),
        ("36-45", "36 to 45 Years"),
        ("46-60", "46 to 60 Years"),
        ("61-65", "61 to 65 Years"),
        ("65+", "65 Years above"),
    ]
      
    ageBand = models.CharField(max_length=10, choices=AGE_BANDS)
    level = models.CharField(max_length=100, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)

    additional_planId=models.ForeignKey(AdditionalPlan, on_delete=models.CASCADE)
    class Meta:
        db_table = "Covrage"
