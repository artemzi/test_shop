from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'city', 'stripe_customer_id')
    list_display_links = ('__unicode__', 'city')
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)