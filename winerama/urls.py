from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^admin/', include(admin.site.urls)),
]
