from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^orders/', include('orders.urls', namespace="orders")),
    url(r'^admin/', include(admin.site.urls)),
]
