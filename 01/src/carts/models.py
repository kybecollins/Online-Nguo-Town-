from django.db import models
from nguo.models import Clothes
# Create your models here.

class Cart(models.Model):
    products = models.ManyToManyField(Clothes,blank=True)
    total = models.DecimalField(max_digits=150,decimal_places=2, default=0.00)
    date_created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return"Cart id: %s" %(self.id)
