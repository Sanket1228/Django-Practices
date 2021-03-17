from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutShop"),
    path('contact/',views.contact,name="Contacts"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path('products/<int:myid>',views.productView,name="productView"),
    path('checkout/',views.checkout,name="checkout")    
]
