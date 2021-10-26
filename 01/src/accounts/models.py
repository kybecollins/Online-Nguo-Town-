from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name   = models.CharField (max_length=200 ,null=True)
    second_name  = models.CharField (max_length=200 ,null=True)
    username     = models.CharField(max_length=30, unique=True)
    phone        = models.CharField (max_length=200 ,null=True)
    email        = models.CharField (max_length=200 ,null=True)
    date_created = models.DateTimeField(auto_now_add = True)


    def __str__(self) :
        return self.username
    
