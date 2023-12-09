from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

def new_book(request):
    parms={
        'title':'本登録ページ',
        'form':PostForm
    }
    if (request.method=='POST'):
        title=request.POST['title']
        print(title)
    return render(request,'form.html',parms)