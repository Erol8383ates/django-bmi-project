from django.db import models

# Create your models here.
from django.db import models

class BMIRecord(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length=50)