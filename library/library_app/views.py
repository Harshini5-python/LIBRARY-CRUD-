
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Book
from . forms import BookForm
# Create your views here.
def index(request):
    book = Book.objects.all()
    context = {
        'book_list': book
    }
    return render(request,"index.html",context)

def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request,"detail.html",{'book':book})

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        book = Book(name=name, desc=desc, img=img)
        book.save()
    return render(request,'add.html')

def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book': book})

def delete(request,id):
    if request.method == 'POST':
        movie = Book.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
