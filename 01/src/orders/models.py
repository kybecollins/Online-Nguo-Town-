from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from carts.models import Cart

User  = get_user_model()
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
    user = models.ForeignKey(User,blank=True ,null=True,on_delete=models.SET_NULL)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_id = models.CharField(max_length = 120, default ="ABC",unique=True)

    # product = models.ForeignKey(Clothes,null=True,on_delete=models.SET_NULL, related_name='orderproduct')
    final_total=  models.DecimalField(default=10.99, max_digits=10000, decimal_places=2)
    location =models.CharField (max_length=200 ,null=True ,choices=LOCATIONS)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField (max_length=300 ,null=True,choices=STATUS, default="Pending")

    def __str__(self):
        return self.order_id