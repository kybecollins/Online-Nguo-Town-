from django.db import models

# Create your models here.
from carts.models import Cart

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
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_id = models.CharField(max_length = 120, default ="ABC",unique=True)
    # customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    # product = models.ForeignKey(Clothes,null=True,on_delete=models.SET_NULL, related_name='orderproduct')
    
    location =models.CharField (max_length=200 ,null=True ,choices=LOCATIONS)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField (max_length=300 ,null=True,choices=STATUS, default="Started")

    def __str__(self):
        return self.order_id