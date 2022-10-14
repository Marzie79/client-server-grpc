from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('customer/', include('customer.urls')),
    path('admin/', admin.site.urls),
]
