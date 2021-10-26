from django import forms
from django.forms import ModelForm
from nguo.models import Clothes

class ClothForm(ModelForm):
    class Meta:
        model = Clothes
        fields = "__all__"