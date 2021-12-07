import time
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from carts.models import Cart
from .models import Order
from .utils import id_generator
from django.contrib.auth.decorators import login_required

# Create your views here.
def order_view(request):
    context = {}
    return render(request,'orders/order.html', context)

@login_required   
def checkout(request):
    try:
        the_id=request.session['cart_Id']
        cart = Cart.objects.get(id=the_id)

    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))
    
    try:
        new_order=Order.objects.get(cart=cart)
        
    except Order.DoesNotExist:
        new_order=Order(cart =cart)
        new_order.user=request.user
        new_order.order_id = id_generator()
        new_order.save()
    
    except:
        return HttpResponseRedirect(reverse("cart"))


    # new_order,created = Order.objects.get_or_create(cart=cart)
    # if created:
    #     new_order.order_id = id_generator()
    #     new_order.save()
    # new_order.user = request.user
    # new_order.save()

    if new_order.status == "Delivered":
        del request.session['cart_Id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))


    context ={}
    return render (request, "orders/checkout.html",context)


