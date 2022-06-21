from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cpu = models.CharField(max_length=255)
    cooler = models.CharField(max_length=255)
    mobo = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    psu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    case = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
