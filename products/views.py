from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from .models import Products


def home(request):
    
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


@login_required
def products(request):
    queryset = Products.objects.all()

    return render_to_response('results.html', locals(), context_instance=RequestContext(request))

def product_single(request, slug):
    product = Products.objects.get(slug=slug)

    return render_to_response('product.html', locals(), context_instance=RequestContext(request))
