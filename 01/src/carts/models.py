from django.db import models
from nguo.models import Clothes
# Create your models here.

class CartItems(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Clothes,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True,blank=True)
    line_total = models.DecimalField(default=10.99, max_digits=10000, decimal_places=2) 
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        try:
            return str(self.cart.id)
        except:
            return str(self.product.title)

class Cart(models.Model):
   
    # items = models.ManyToManyField(CartItems,blank=True)
    total = models.DecimalField(max_digits=150,decimal_places=2, default=0.00)
    date_created = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return"Cart id: %s" %(self.id)
