# Generated by Django 2.2.6 on 2019-11-04 02:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('cartid', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='product.ProductVariant')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(blank=True, to='cart.CartItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]