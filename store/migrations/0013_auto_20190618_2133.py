# Generated by Django 2.2.1 on 2019-06-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20190618_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastorders',
            name='order_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pastorders',
            name='restname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
