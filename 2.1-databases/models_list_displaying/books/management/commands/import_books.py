import json
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', encoding='UTF-8') as jsonfile:
            books_list = json.load(jsonfile)

        for book in books_list:
            book_row = Book(name=book['fields']['name'],
                            author=book['fields']['author'],
                            pub_date=datetime.strptime(book['fields']['pub_date'], '%Y-%m-%d'))
            book_row.save()
