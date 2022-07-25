import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_row = Phone(id=phone['id'],
                              name=phone['name'],
                              price=int(phone['price']),
                              image=phone['image'],
                              release_date=phone['release_date'],
                              lte_exists=phone['lte_exists'],
                              slug=slugify(phone['name']))
            phone_row.save()
