# Generated by Django 2.2.1 on 2019-06-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190618_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodorder',
            name='foid',
        ),
        migrations.AddField(
            model_name='foodorder',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
