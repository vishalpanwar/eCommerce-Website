from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length = 120)
    email = models.EmailField(max_length = 200)
    message = models.CharField(max_length = 500)
    timestamp = models.DateTimeField(default = datetime.datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        # most recent first
        ordering = ['-timestamp']