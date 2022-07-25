from datetime import datetime

from django.db.models import Max, Min
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    for book in books_list:
        book.pub_date = datetime.strftime(book.pub_date, '%Y-%m-%d')
    context = {'books': books_list}
    return render(request, template, context)


def book_details(request, pub_date):
    template = 'books/book.html'
    books_list = Book.objects.filter(pub_date=pub_date)
    for book in books_list:
        book.pub_date = datetime.strftime(book.pub_date, '%Y-%m-%d')
    has_previous = Book.objects.filter(pub_date__lt=pub_date)
    if has_previous:
        prev_date = datetime.strftime(has_previous.aggregate(Max('pub_date'))['pub_date__max'], '%Y-%m-%d')
    else:
        prev_date = None
    has_next = Book.objects.filter(pub_date__gt=pub_date)
    if has_next:
        next_date = datetime.strftime(has_next.aggregate(Min('pub_date'))['pub_date__min'], '%Y-%m-%d')
    else:
        next_date = None
    context = {'books': books_list,
               'prev_date': prev_date,
               'next_date': next_date,
               }
    return render(request, template, context)
