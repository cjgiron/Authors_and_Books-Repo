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