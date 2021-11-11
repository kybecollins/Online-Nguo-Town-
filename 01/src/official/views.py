from django.http.response import Http404
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView
from official.forms import ClothForm
from nguo.models import Clothes
from carts.models import Cart,CartItems


from django.urls import reverse

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


def contact_view(request):
    return render(request,'official/contact.html')


def cart_view(request):
    try:
        the_id=request.session['cart_Id']

    except:
        the_id = None
    
    if the_id:
        cart =Cart.objects.get(id =the_id)
        context = {
            "cart":cart,
            }
    else:
        empty_message = "The Cart is Empty, kwani hauna Doo!"
        context = {
            'empty':True,
            'empty_message': empty_message,
                }

    return render(request,'official/cart.html',context)

def update_cart_view(request,slug):

    request.session.set_expiry(60480) #resets cart after 1 week

    try:
        the_id=request.session['cart_Id']

    except:
        new_cart =Cart()
        new_cart.save()
        request.session['cart_Id'] = new_cart.id
        the_id = new_cart.id

    cart =Cart.objects.get(id =the_id)

    try:
        product = Clothes.objects.get(slug=slug)
    except Clothes.DoesNotExist:
        pass
    except:
        pass
    cart_item, created =CartItems.objects.get_or_create(cart=cart,product=product)

    # if qty ==0:
    #     cart_item.delete()
    # else:s
    #     cart_item.save()


    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)



    cart_price  = 0.00
    for item in cart.cartitems_set.all():
        total_line = float(item.product.price) * item.quantity

        cart_price += total_line

    request.session['items_total'] = cart.cartitems_set.count()
    cart.total = cart_price
    cart.save()

    return HttpResponseRedirect(reverse("cart"))

def detail_view(request,slug):
    try:
        product = Clothes.objects.get(slug=slug)
        context={
            'product':product,
        }
        return render(request,'official/detail.html',context)
    except:
        raise Http404



