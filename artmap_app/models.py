from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=127)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    details_url = models.URLField(default='')

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

    @staticmethod
    def prepare_geodata(top_slice=1000):
        features = [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat],

                },
                'properties': {
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': place.details_url,
                }
            }
            for place in Place.objects.order_by('-pk').all()[:top_slice]     # top new objects
        ]

        geodata = {
            "type": "FeatureCollection",
            "features": features,
        }
        return geodata


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    position_in_order = models.PositiveSmallIntegerField(default=0)
    pict = models.ImageField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('place', 'position_in_order'), name='unique_position'),
        ]

    def __str__(self):
        return f'{self.position_in_order} in {self.place.title}'
