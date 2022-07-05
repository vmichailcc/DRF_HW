from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
