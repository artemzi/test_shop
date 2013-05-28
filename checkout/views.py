from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

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
        info = request.user.get_profile()
    except:
        user = User.objects.get(request.user)
        info = userProfile(user)
        info.save()



    return render_to_response('checkout/checkout.html', locals(),
                                context_instance=RequestContext(request))
