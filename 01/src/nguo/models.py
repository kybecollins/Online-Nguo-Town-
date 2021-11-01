
from django.db import models
from accounts.models import Customer

# Create your models here.
class Tag(models.Model):
    name =models.CharField (max_length=200 ,null=True)

    def __str__(self) :
        return self.name


class Clothes(models.Model):
    LOCATIONS = (
        ('Nairobi', 'Nairobi'),
        ('Thika', 'Thika'),
        ('Mombasa','Mombasa'),

    )
    CLOTHTYPES=(
        ('Jacket','Jacket'),
        ('Shirt','Shirt')
    )
    name =models.CharField (max_length=200 ,null=True)
    price = models.CharField (max_length=200 ,null=True)
    cloth_type = models.CharField (max_length=200 ,null=True ,choices=CLOTHTYPES)
    location =models.CharField (max_length=200 ,null=True ,choices=LOCATIONS)
    description = models.CharField (max_length=300 ,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null =True ,blank =True,upload_to ='images/')

    def __str__(self) :
        return self.name




class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Shipping', 'Shipping'),
        ('Delivered','Delivered'),

    )
    LOCATIONS = (
        ('Nairobi', 'Nairobi'),
        ('Thika', 'Thika'),
        ('Mombasa','Mombasa'),

    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Clothes,null=True,on_delete=models.SET_NULL, related_name='orderproduct')
    # location_order =models.ForeignKey(Clothes,null=True,on_delete=models.SET_NULL,related_name='locationorders')
    location =models.CharField (max_length=200 ,null=True ,choices=LOCATIONS)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField (max_length=300 ,null=True,choices=STATUS)
    



