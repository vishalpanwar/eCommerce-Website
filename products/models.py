from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 120)
    # as we are using get to filter out slug in product.views
    slug = models.SlugField(unique = True)
    description = models.CharField(max_length = 300, blank = True, null = True)
    image1 = models.ImageField(upload_to = 'product_images',blank = True, null = True)

    def __unicode__(self):
        return self.name + " : " + self.description

    # To reverse the ordering a/c to negative of name/id in the query set
    class Meta:
        ordering = ['-name']
