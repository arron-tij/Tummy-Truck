# Generated by Django 2.2.1 on 2019-06-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20190618_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='sale',
            field=models.IntegerField(null=True),
        ),
    ]
