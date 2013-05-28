from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from cart.models import Cart
from customers.models import UserProfile

import stripe

stripe.api_key = 'sk_test_OfbJCPliyi7Rfu4ajj0JQrdU'


def checkout(request):
    try:
        cart_id = request.session['cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        return HttpResponseRedirect('/cart/')

    try:
        user = User.objects.get(id=request.user.id)
    except:
        return HttpResponseRedirect('/')

    profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
        print "{} was created".format(profile)

    try:
        customer = stripe.Customer.retrieve(str(profile.stripe_customer_id))
    except:
        customer = stripe.Customer.create(email=request.user.email)
        profile.stripe_customer_id = customer.id
        profile.save()

    return render_to_response('checkout/checkout.html', locals(),
                            context_instance=RequestContext(request))
