from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from profiles.models import UserProfile
from checkout.models import Order


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    stock_level = models.IntegerField(validators=[MinValueValidator(0)],
                                      null=False, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product_Review(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    rating = models.IntegerField(validators=[MaxValueValidator(5),
                                             MinValueValidator(0)],
                                 null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
