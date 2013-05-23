from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user', 'total_price', 'active', 'timestamp')
    list_display_links = ('__unicode__', 'user')
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)