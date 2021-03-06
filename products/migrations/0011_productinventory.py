# Generated by Django 3.1.2 on 2020-11-13 16:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productreview_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(editable=False, max_length=32)),
                ('stock_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
