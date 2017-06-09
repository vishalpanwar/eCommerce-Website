from django.contrib import admin

# Register your models here.

from .forms import ContactUsForm
from .models import ContactUs
from .forms import ContactUsForm

class ContactAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','timestamp')
    form = ContactUsForm

admin.site.register(ContactUs, ContactAdmin)


