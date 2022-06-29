from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.timezone import datetime
from django.contrib import messages


# Create your views here.
from App_main.models import CartModel, IngredientModel, PrepareModel


def home(request):
    my_cart = CartModel.objects.filter(customer=request.user).count()
    content = {
        'my_cart': my_cart,
    }
    return render(request, 'App_main/home.html', context=content)


def prepare(request):
    my_cart = CartModel.objects.filter(customer=request.user).count()
    ingredients_bun = IngredientModel.objects.filter(category='bun')
    ingredients_patty = IngredientModel.objects.filter(category='patty')
    ingredients_veg = IngredientModel.objects.filter(category='veg')
    ingredients_addon = IngredientModel.objects.filter(category='addon')
    ingredients_sauce = IngredientModel.objects.filter(category='sauce')
    ingredients_mayo = IngredientModel.objects.filter(category='mayo')
    if request.method == 'POST':
        all_ids = request.POST.get('all_ids')
        item_list = list(map(str, all_ids.split(',')))
        item_list.pop()
        total_price = 0
        model_list = []
        cat_list = []
        for i in item_list:
            this_item = IngredientModel.objects.get(id=int(i))
            item_name = this_item.item
            if this_item.category == 'bun':
                cat_list.append(1)
            if this_item.category == 'patty':
                cat_list.append(2)
            if this_item.category == 'veg':
                cat_list.append(3)
            if this_item.category == 'sauce':
                cat_list.append(4)
            if this_item.category == 'addon':
                cat_list.append(5)
            total_price += this_item.price
            model_list.append(item_name)
        my_set = set(cat_list)
        if 1 in my_set and 2 in my_set:
            my_model = PrepareModel(items=model_list, b_price=total_price)
            my_model.save()
            new_cart = CartModel(customer=request.user, order=my_model, total_price=total_price)
            new_cart.save()
        else:
            messages.error(request, f'You have to choose from the Required Bun And Patty field!')
        return HttpResponseRedirect(reverse('App_main:prepare'))
    content = {
        'my_cart': my_cart,
        'ingredients_bun': ingredients_bun,
        'ingredients_patty': ingredients_patty,
        'ingredients_addon': ingredients_addon,
        'ingredients_veg': ingredients_veg,
        'ingredients_sauce': ingredients_sauce,
    }
    return render(request, 'App_main/prepare.html', context=content)


def cart_view(request):
    my_cart = CartModel.objects.filter(customer=request.user)
    if request.method == 'POST' and 'update' in request.POST:
        update = request.POST.get('quantity')
        up = request.POST.get('up')
        cart = CartModel.objects.get(id=up)
        cart.quantity = update
        cart.save()

    content = {
        'my_cart': my_cart.count(),
        'carts': my_cart,
    }
    return render(request, 'App_main/cart.html', context=content)


def delete_sys(request, pk):
    cart = CartModel.objects.get(id=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('App_main:cart'))