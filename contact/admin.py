from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'message')
    list_display_links = ('__unicode__', 'name')
    class Meta:
        model = ContactUs

admin.site.register(ContactUs, ContactUsAdmin)