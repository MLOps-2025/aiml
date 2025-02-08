from django.db import models # type: ignore

# Create your models here.

class aiml(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.IntegerField()
    region = models.IntegerField()
    charges = models.FloatField()
