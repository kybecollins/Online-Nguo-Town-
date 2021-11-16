from django.contrib import admin

# Register your models here.
from nguo.models import Clothes,Tag

# admin.site.register(Clothes)

admin.site.register(Tag)

class TitleSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Clothes, TitleSlug)