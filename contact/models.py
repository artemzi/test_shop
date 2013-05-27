import datetime
from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=300)
    message = models.TextField(max_length=600)
    timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ['-timestamp']
        verbose_name = ('Contuct Us')
        verbose_name_plural = ('Contucting Us')