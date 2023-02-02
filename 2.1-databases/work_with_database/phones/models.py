from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    
 

