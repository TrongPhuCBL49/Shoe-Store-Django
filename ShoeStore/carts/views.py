from django.shortcuts import render, redirect

from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from authen.forms import GuestForm
from authen.models import GuestEmail

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
    user = request.user
    billing_profile = None
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
            user = user, email = user.email)
    elif guest_email_id is not None:
        guest_email_object = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(
            email = guest_email_object.email)
    else:
        pass
    if billing_profile is not None:
        order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if order_qs.count() == 1:
            order_obj = order_qs.first()
        else:
            old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

    context = { 
        "object": order_obj,
        "billing_profile": billing_profile,
        "guest_form": guest_form,
    }
    return render(request, "carts/checkout.html", context)
