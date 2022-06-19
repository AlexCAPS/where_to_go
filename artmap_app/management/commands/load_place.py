import json
from argparse import FileType
from io import TextIOWrapper

from django.core.management import BaseCommand
from django.db import transaction

from artmap_app.models import Place, Image
from artmap_app.utils import download_image


class Command(BaseCommand):
    help = 'Load place from file(s)'

    def add_arguments(self, parser):
        parser.add_argument('place_dump_files', nargs='+', type=FileType('r'))

    def handle(self, *args, **options):
        for dumped_place in options['place_dump_files']:
            try:
                self.import_place(dumped_place)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'The changes have not been applied. '
                                                   f'File "{dumped_place.name}" was skipped.'))
                self.stdout.write(self.style.ERROR(e))

        self.stdout.write(self.style.SUCCESS('Import completed'))

    @transaction.atomic
    def import_place(self, dumped_place: TextIOWrapper):
        place_content = json.load(dumped_place)

        place = Place.load_place(place_content)

        if not place:
            self.stdout.write(self.style.WARNING(f'File "{dumped_place.name}" was skipped.'))
            return

        self.stdout.write(self.style.SUCCESS(f'Ploace from file "{dumped_place.name}" was loaded.'))

        for position, image_url in enumerate(place_content.get('imgs', [])):
            image_content = download_image(image_url)
            image = Image.load_image(place, image_content, position)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {image.pict.url}.'))
