from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, 'index.html', context)


def process_book(request):
    print(request.POST)

    Book.objects.create(
        title = request.POST['book_title'],
        description = request.POST['book_description'],
    )

    return redirect('/')

def delete(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_book.delete()

    return redirect('/')


def delete_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_author.delete()

    return redirect('/authors')


def display(request, book_id):
    this_book = Book.objects.get(id=book_id)

    context = {
        'book': this_book,
        'authors': Author.objects.all(),
    }

    return render(request, 'display_book.html', context)


def display_author(request, author_id):
    this_author = Author.objects.get(id=author_id)

    context = {
        'author': this_author,
        'books': Book.objects.all()
    }

    return render(request, 'display_author.html', context)

def add_author(request):
    print(request.POST)

    author_id = request.POST['author']
    book_id = request.POST['book_id']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)

    book.authors.add(author)

    return redirect(f'books/{book_id}/display')


def add_book(request):
    print(request.POST)

    author_id = request.POST['author_id']
    book_id = request.POST['book']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)

    author.books.add(book)

    return redirect(f'authors/{author_id}/display')


def authors(request):
    context = {
        'all_authors': Author.objects.all(),
    }

    return render(request, 'authors.html', context)


def process_author(request):
    print(request.POST)

    Author.objects.create(
        first_name = request.POST['author_first_name'],
        last_name = request.POST['author_last_name'],
        notes = request.POST['author_notes']
    )

    return redirect('/authors')