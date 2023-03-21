from enum import unique
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=191, unique=True)
    expiration_duration = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField()


    def __str__(self):
        return self.name



class Purchase( models.Model ):
  '''purchases'''
  resource = models.ForeignKey("videos.Video", on_delete=models.CASCADE)
  purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
  purchased_at = models.DateTimeField(auto_now_add=True)
  tx = models.CharField(max_length=250)


  def __str__(self):
    return f"{self.purchaser}"
 