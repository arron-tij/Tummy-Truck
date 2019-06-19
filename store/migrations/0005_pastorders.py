# Generated by Django 2.2.1 on 2019-06-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190618_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poid', models.IntegerField(default=0, null=True)),
                ('foodorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.FoodOrder')),
            ],
        ),
    ]
