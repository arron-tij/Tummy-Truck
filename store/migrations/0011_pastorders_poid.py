# Generated by Django 2.2.1 on 2019-06-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_pastorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastorders',
            name='poid',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
