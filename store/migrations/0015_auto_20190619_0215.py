# Generated by Django 2.2.1 on 2019-06-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_food_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='sale',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
