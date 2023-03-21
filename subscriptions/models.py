from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


class Subscription(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    subscription_type =models.CharField(max_length=20,choices=(("monthly", "monthly"), ("three_months", "three_months"),("six_months", "six_months"), ("yearly", "yearly")))

    def __str__(self):
        return f"{self.timestamp}"