from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context

from .forms import ContactUsForm

# Create your views here.

def contact_page(request):
    print("In contact page")
    form = ContactUsForm(request.POST or None)
    print(form.errors)
    if form.is_valid():
        this_form = form.save(commit = False)
        print("form not saved yet!")
        this_form.save()
        return HttpResponseRedirect('/')
    else:
        print("form not valid")
    return render(request,'contact/form.html',locals())
