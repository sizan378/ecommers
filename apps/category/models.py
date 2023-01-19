from django.db import models
from apps.common.models import TimeStampedUUIDModel, ActiveTable


class Category(TimeStampedUUIDModel, ActiveTable):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'
