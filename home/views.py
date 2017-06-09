from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

def home_page(request):
    return render(request,'home.html',locals())

# Create your views here.
