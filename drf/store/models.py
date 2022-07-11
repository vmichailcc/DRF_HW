from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(max_length=800, verbose_name="Description")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                         verbose_name="Rating")
    owner = models.ForeignKey(
        'auth.User',
        related_name='stores',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(
        choices=(
            ("in_review", "In Review"),
            ("active", "Active"),
            ("deactivated", "Deactivated"),
        ),
        max_length=11,
        default="in_review"
    )

    class Meta:
        ordering = ["-id"]
