import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'products.views.home'),
    url(r'^products/$', 'products.views.products', name='products'),
    url(r'^products/(?P<slug>[-\w]*)/$', 'products.views.product_single'),
    url(r'^products/(?P<slug>[-\w]*)/add$', 'cart.views.add'),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^cart/$', 'cart.views.view'),
    url(r'^cart/delete$', 'cart.views.delete'),
    # url(r'^shopping/', include('shopping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Static files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ('^pages/', include('django.contrib.flatpages.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^accounts/', include('registration.backends.default.urls')),
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
