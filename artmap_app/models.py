from hashlib import md5

from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=127)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)

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

    def to_dict(self):
        return {
            'title': self.title,
            'imgs': [img.pict.url for img in self.images.all()],
            'description_short': self.description_short,
            'description_long': self.description_long,
            'coordinates': {
                'lng': self.lng,
                'lat': self.lat,
            },
        }

    @staticmethod
    def load_place(place_content: dict):
        try:
            place, created = Place.objects.get_or_create(
                title=place_content['title'],
                defaults={
                    'title': place_content['title'],
                    'description_short': place_content['description_short'],
                    'description_long': place_content['description_long'],
                    'lat': place_content['coordinates']['lat'],
                    'lng': place_content['coordinates']['lng'],
                })
        except MultipleObjectsReturned:
            return None

        return place if created else None


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position_in_order = models.PositiveSmallIntegerField(default=0)
    pict = models.ImageField(upload_to='places')

    class Meta:
        ordering = ['position_in_order']

    def __str__(self):
        return f'{self.position_in_order} in {self.place.title}'

    @staticmethod
    def load_image(place: Place, image_content: bytes, position: int):
        # create image object in db
        content_file = ContentFile(image_content, name=md5(image_content).hexdigest())
        image = Image.objects.create(place=place, pict=content_file, position_in_order=position)

        return image

