# Generated by Django 3.2.3 on 2021-08-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0003_preparemodel_b_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientmodel',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
