from django.contrib import admin

# Register your models here.
from nguo.models import Clothes,Order,Tag

admin.site.register(Clothes)
admin.site.register(Order)
admin.site.register(Tag)