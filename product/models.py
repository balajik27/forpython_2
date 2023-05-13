from django.db import models

# Create your models here.

class User_Details(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    mobile = models.IntegerField()
    country = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username

# class Address(models.Model):




