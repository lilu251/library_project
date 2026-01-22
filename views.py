from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Home page
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

# Book create page
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def about(request):
    return render(request, 'books/about.html')

def services(request):
    return render(request, 'books/services.html')

def rules(request):
    return render(request, 'books/rules.html')

def contact(request):
    return render(request, 'books/contact.html')