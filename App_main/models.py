
from django.db import models
from django_mysql.models import ListCharField


# Create your models here.
from App_login.models import CustomUser


class IngredientModel(models.Model):
    item = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='ingredient_images')
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)


class PrepareModel(models.Model):
    items = ListCharField(base_field=models.CharField(max_length=50), size=20, max_length=(20 * 51))
    b_price = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now=True)


class CartModel(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='buyer')
    order = models.ForeignKey(PrepareModel, on_delete=models.CASCADE, related_name='each_order')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)

    def get_price(self):
        total_price = self.quantity * round(self.order.b_price)
        return format(total_price, "0.2f")



class OrderModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_user')
    my_cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name='carts')
    created = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    sub_total = models.PositiveIntegerField(default=0)
