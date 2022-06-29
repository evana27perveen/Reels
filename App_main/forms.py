from django.contrib.auth.forms import forms
from App_main.models import *


class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ['quantity', ]


