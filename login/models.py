from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.AutoField
    first_name = models.CharField(max_length = 50, default ="")
    last_name = models.CharField(max_length = 50, default ="", null = 'False')
    user_name = models.CharField(max_length = 50, default ="")
    password = models.CharField(max_length = 59,default="")

def __str__(self):
    return self.user_name
