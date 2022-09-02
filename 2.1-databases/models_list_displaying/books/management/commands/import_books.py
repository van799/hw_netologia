import json

from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', encoding='utf-8') as file:
            books = json.load(file)
            for book in books:
                obj = Book(
                    id=book['pk'],
                    name=book['fields']['name'],
                    author=book['fields']['author'],
                    pub_date=book['fields']['pub_date'],
                )
                obj.activated = True
                obj.save()
