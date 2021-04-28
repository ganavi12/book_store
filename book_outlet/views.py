from django.shortcuts import render,get_object_or_404
from .models import Book
from django.http import Http404

# Create your views here.
def index(request):
    try:
        books = Book.objects.all()
    except:
        raise Http404()

    return render(request, 'book_outlet/index.html', {"books": books})
    
def book_detail(request,id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    # or

    book = get_object_or_404(Book,pk=id)
    return render(request, 'book_outlet/book_detail.html', {"title": book.title,"rating": book.rating,"author": book.author,"is_bestselling":book.is_bestselling})