
from django.urls import path

from .views import SearchStuff

urlpatterns = [
    path('stuff/<str:query>/', SearchStuff.as_view()),
]