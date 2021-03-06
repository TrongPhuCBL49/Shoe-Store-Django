from django.shortcuts import render, redirect

from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from authen.models import GuestEmail

from authen.forms import GuestForm
from addresses.forms import AddressForm

from .models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    request.session['cart_items'] = cart_obj.products.count()
    return render(request, "carts/cart.html", {"cart": cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    print(product_id)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("carts:cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
        request.session['cart_items'] = cart_obj.products.count()
    # return redirect(product_obj.get_absolute_url())
    # return redirect(request.get_full_path())
    return redirect(request.POST.get('current_url'))

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
    context = { 
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form": guest_form,
        "address_form": address_form,
    }
    return render(request, "carts/checkout.html", context)
