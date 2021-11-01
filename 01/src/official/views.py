from django.shortcuts import render
from django.views.generic import CreateView
from official.forms import ClothForm
from nguo.models import Clothes
from carts.models import Cart

# Create your views here.
def default_home_view(request):
    return render(request,'official/home.html')

def shopping_view(request):
    cloth = Clothes.objects.all()
    context = {
        'cloth': cloth
    }
    return render(request,'official/shopping.html',context)


def posting_view(request):
    

   
    if request.method == 'POST' :
        form= ClothForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form= ClothForm

    context = {
        'form' : form
    }
    return render(request,'official/post.html',context)

# class postingView(CreateView):
#     model = Clothes
#     template_name = 'post.html'
#     fields = '__all__'
def contact_view(request):
    return render(request,'official/contact.html')


def cart_view(request):
    cart =Cart.objects.all()[0]
    context = {
        "cart":cart,
    }
    return render(request,'official/cart.html',context)