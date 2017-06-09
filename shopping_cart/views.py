from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .models import ShoppingCart
from products.models import Products

# Create your views here.

def add(request,slug):
    product_add = Products.objects.get(slug = slug)
    request.session.set_expiry(300)

    try:
        active = request.session['cart']
    except:
        request.session['cart'] = 'Empty'

    if request.session['cart'] != 'Empty':
        cart = request.session['cart']
        update_cart = ShoppingCart.objects.get(id = cart)
        update_cart.products.add(product_add)
        update_cart.save()
        request.session['total_items'] = len(update_cart.products.all())
    else:
        # making new cart object and save it
        new_shopping_cart = ShoppingCart()
        new_shopping_cart.save()
        new_shopping_cart.products.add(product_add)
        new_shopping_cart.save()
        request.session['cart'] = new_shopping_cart.id
        request.session['total_items'] = len(new_shopping_cart.products.all())


    #s = '/products/' + str(slug)
    return HttpResponseRedirect('/products/' + slug)



def cart_view(request):

    cart = False
    mssg = 'Hello world!'

    try:
        cart_id = request.session['cart']
        cart_exists = ShoppingCart.objects.get(id = cart_id)
    except:
        cart_exists = False
        try:
            request.session['total_items'] == 0
        except:
            pass

    if cart_exists == False or cart_exists.active is False:
        mssg = 'Your cart is empty!'

    if cart_exists and cart_exists.active:
        cart = cart_exists

    return render(request,'cart/cart.html',{'cart_exists': cart, 'mssg': mssg})



def cart_empty(request):

    try:
        cart_id = request.session['cart']
        cart_exists = ShoppingCart.objects.get(id = cart_id)
    except:
        cart_exists = False
        pass
    print('>>>>>>>>>>>>>>>>',cart_exists)

    if cart_exists:
        cart = ShoppingCart.objects.get(id = cart_id)
        cart.active = False
        cart.save()
        request.session['total_items'] = 0
        request.session['cart'] = 'Empty'
        #request.session['cart'] = 'Empty'

        return HttpResponseRedirect('/cart/')
