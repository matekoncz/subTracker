from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=128, primary_key=True)
    description = models.TextField(max_length=256)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "user"), name="cat_unique_for_user"
            ),
        ]

class Subscription(models.Model):
    service_name = models.TextField(max_length=128, primary_key=True)
    price = models.FloatField()
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("service_name", "user"), name="sub_unique_for_user"
            ),
        ]