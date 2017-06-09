from datetime import date

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .models import Products

# Create your views here.

def product_page(request):
    queryset = Products.objects.all()
    name = 'vishal'
    return render(request,'results.html',locals())

def product_single(request, slug):
    # if we use filter, we get a list of slug
    # so we use get, which returns a single item
    # i.e. we have multiple slugs, get will give an error while filter will return list
    query = Products.objects.get(slug = slug)
    return render(request,'product.html',{'query':query, 'slug' : slug})
