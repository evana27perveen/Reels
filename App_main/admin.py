from django.contrib import admin
from App_main.models import *

# Register your models here.

admin.site.register(IngredientModel)
admin.site.register(PrepareModel)
admin.site.register(CartModel)
admin.site.register(OrderModel)
