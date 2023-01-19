from django.db import models
from django.contrib.auth.models import User

from apps.category.models import Category
from apps.common.models import TimeStampedUUIDModel, ActiveTable


class Product(TimeStampedUUIDModel, ActiveTable):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "product"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
