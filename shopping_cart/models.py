from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from products.models import Products

import datetime

# Create your models here.

class ShoppingCart(models.Model):
    user = models.ForeignKey(User,null = True,blank = True)
    total_price = models.CharField(max_length = 120, default = 0)
    active = models.BooleanField(default = True)
    products = models.ManyToManyField(Products,null = True, blank = True)
    timestamp = models.DateTimeField(default = timezone.now(), editable = False)

    def __unicode__(self):
        return str(self.id)
