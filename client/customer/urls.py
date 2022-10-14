from django.urls import path

from . import views

urlpatterns = [
    path('price/', views.get_price, name='get_price'),
    path('seller/', views.get_seller, name='get_seller'),
    path('same_stuff/', views.get_same_stuff, name='get_same_stuff'),
    path('stuff/', views.get_stuff, name='get_stuff'),
]