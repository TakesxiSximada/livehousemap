from django.conf.urls import patterns, include, url
from .views import index

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'', index),
)
