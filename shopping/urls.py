"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url, include
from django.contrib import admin
from shopping import settings
from django.views.static import serve
from django.conf.urls.static import static

from products.views import product_page, product_single
from home.views import home_page
from contact.views import contact_page
from shopping_cart.views import add, cart_view, cart_empty

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/$', product_page, name = 'product_page'),
    url(r'^home/$',home_page,name = 'home_page'),
    url(r'^$',home_page,name = 'home_poage'),
    url(r'^contact/$',contact_page,name = 'contact_page'),

    url(r'^pages/', include('django.contrib.flatpages.urls')),

    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    #url(r'^static(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}),

    url(r'^products/(?P<slug>[-\w]+)/$',product_single,name = 'product_single'),
    url(r'^products/(?P<slug>[-\w]+)/add$',add,name = 'shopping_cart_add'),
    url(r'^cart/$',cart_view,name = 'shopiing_cart_view'),
    url(r'^empty/$',cart_empty,name = 'shopping_cart_empty'),
]

# debug environment
# not used in production
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)