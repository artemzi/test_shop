from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']
