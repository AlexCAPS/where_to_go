import json
from argparse import FileType

from django.core.management import BaseCommand
from django.db import transaction

from artmap_app.models import Place, Image
from artmap_app.utils import download_image, download_place_file


class Command(BaseCommand):
    help = 'Load place from file(s)'

    def add_arguments(self, parser):
        parser.add_argument('place_dump_files', nargs='+', type=self.__json_source)

    def handle(self, *args, **options):
        for dumped_place in options['place_dump_files']:
            try:
                self.import_place(dumped_place)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'The changes have not been applied. '
                                                   f'File "{dumped_place.name}" was skipped.'))
                self.stdout.write(self.style.ERROR(e))

        self.stdout.write(self.style.SUCCESS('Import completed'))

    @staticmethod
    def __json_source(arg_string):
        if arg_string.startswith('http'):
            return download_place_file(arg_string)
        else:
            return json.load(FileType('r')(arg_string))

    @transaction.atomic
    def import_place(self, place_content: dict):
        place = Place.load_place(place_content)

        if not place:
            self.stdout.write(self.style.WARNING('Place passed'))
            return

        self.stdout.write(self.style.SUCCESS('Place info loaded'))

        for position, image_url in enumerate(place_content.get('imgs', [])):
            image_content = download_image(image_url)
            image = Image.load_image(place, image_content, position)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {image.pict.url}'))
