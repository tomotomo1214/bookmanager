from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Book, Bookshelf

def new_book(request):
    parms={
        'title':'本登録ページ',
        'form':PostForm
    }
    if (request.method=='POST'):
        title=request.POST['title']
        detail=request.POST['detail']
        bookshelf_id=request.POST['bookshelf']
        print(title)
        print(detail)
        print(bookshelf_id)
        Book.objects.create(title=title, detail=detail, bookshelf=Bookshelf.objects.get(id=bookshelf_id))
    return render(request,'form.html',parms)
def new_bookshelf(request):
    parms={
        'title':'本棚登録ページ',
        'form':PostForm
    }
    