from django.contrib import admin
from store.models import *
# Register your models here.
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(FoodOrder)
admin.site.register(PastOrders)
