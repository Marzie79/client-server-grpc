from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('service/', include('service.urls')),
    path('admin/', admin.site.urls),
]