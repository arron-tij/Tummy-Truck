from django.contrib import admin
from django.urls import path
from store.views import *
urlpatterns = [
    path('profile/', profileView, name="profileView"),
    path('', index, name="index"),
    path('cities/<slug:qcity>',restaurants_view,name='restaurants_view' ),
    path('restaurants/<int:rt>/',restaurant_foods,name='restaurant_foods' ),
    path('restaurants/add/',food_cart,name='food_cart' ),
    path('restaurants/checkout/',checkout,name='checkout' ),
    path('cities/',placeView,name='placeView' ),
    path('past/',pastView,name='pastView' ),
    path('rate_rest/',rate_restaurant,name='rate_restaurant' ),
    path('rate/',rate,name='rate' ),
        
]