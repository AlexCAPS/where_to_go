from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=127)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()

    lng = models.DecimalField(
        max_digits=17,
        decimal_places=14,
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0),
        ]
    )

    lat = models.DecimalField(
        max_digits=16,
        decimal_places=14,
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0),
        ]
    )

    def __str__(self):
        return self.title

