from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from random import randint


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

    # private method available only to Product Class
    def _generate_sku_number(self):
        """
        Generate a random, unique 10 digit SKU number starting with CB
        """
        range_start = 10**(10-1)
        range_end = (10**10)-1
        sku_num = randint(range_start, range_end)
        sku_str = "CB"+str(sku_num)
        return sku_str

    def save(self, *args, **kwargs):
        """
        Override the product save method to generate the SKU number
        if it hasn't been set already.
        """
        if not self.sku:
            self.sku = self._generate_sku_number()
        super().save(*args, **kwargs)


class ProductReview(models.Model):
    review_id = models.CharField(max_length=254, null=True, blank=True)
    user = models.CharField(max_length=254, null=False)
    product = models.CharField(max_length=254, null=False)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(5)],
                                 null=False, default=0)
    review = models.TextField()
    timestamp = models.CharField(max_length=254, null=True)

    # private method available only to ProductReview Class
    def _generate_review_number(self):
        """
        Generate a random, unique 10 digit Product Review
        (PR) number starting with PR
        """
        range_start = 10**(10-1)
        range_end = (10**10)-1
        pr_num = randint(range_start, range_end)
        pr_str = "PR"+str(pr_num)
        return pr_str

    def save(self, *args, **kwargs):
        """
        Override the save method to generate the PR number number
        """
        if not self.review_id:
            self.review_id = self._generate_review_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.review_id
