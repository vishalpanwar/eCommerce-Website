from django.contrib import admin

from .models import ShoppingCart

# Register your models here.

class ShoppingCartAdmin(admin.ModelAdmin):
    class Meta:
        model = ShoppingCart

admin.site.register(ShoppingCart,ShoppingCartAdmin)