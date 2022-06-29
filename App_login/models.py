from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


# Create your models here.

gender_choice = (
    ('male', 'Male'),
    ('Female', 'Female'),
    ('Third Gender', 'Third Gender')
)


class CustomUser(AbstractUser):
    phone_number = PhoneField(blank=False, help_text='Contact phone number')
    gender = models.CharField(choices=gender_choice, max_length=12)
    dob = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='photos/profile_picture')

    def __str__(self):
        return f'{self.username}'
