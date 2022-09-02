from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def book_date(request, slug):
    template = 'books/books_date.html'
    book = Book.objects.filter(pub_date=slug)

    books = Book.objects.all()
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'book_date': page_obj,
        'page_obj': page_obj
    }
    return render(request, template, context)
