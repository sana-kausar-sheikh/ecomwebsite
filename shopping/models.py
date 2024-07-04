from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    def __str__(self) -> str:
        return self.title
        
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=400)

