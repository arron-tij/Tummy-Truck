# Generated by Django 2.2.1 on 2019-06-18 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_pastorders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastorders',
            name='foodorder',
        ),
    ]