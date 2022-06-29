from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from App_login.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['pk', 'first_name', 'last_name', 'username', 'email']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ['phone_number', 'gender', 'dob', 'profile_picture']}),

    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['phone_number', 'gender', 'dob', 'profile_picture']}),

    )


admin.site.register(CustomUser, CustomUserAdmin)
