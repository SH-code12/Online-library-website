from django.shortcuts import render
from .models import LogIn
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from .models import Books
from .models import User

# Create your views here.

# def Log(request):
#     return render(request, 'UserBooks/Log.html')

def UserBooks(request):
    books = Books.objects.all()
    return render(request, 'Pages/ViewBook_User.html', {'books': books} )

def Borrow(request):
    if request.method == 'POST' and 'book_id' in request.POST:
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Books, pk=book_id)
        book.status = 'Borrowed' 
        book.save()
        return JsonResponse({'message': 'Book Borrowed successfully'})
    else:
        borrow_books = Books.objects.filter(status='Borrow')
        return render(request, 'Pages/Borrow.html', {'borrow_books': borrow_books})

def BorrowedBooks(request):
    if request.method == 'POST' and 'book_id' in request.POST:
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Books, pk=book_id)
        book.status = 'Borrow'  
        book.save()
        return JsonResponse({'message': 'Book returned successfully'})
    else:
        borrowed_books = Books.objects.filter(status='Borrowed')
        return render(request, 'Pages/BorrowedBooks.html', {'borrowed_books': borrowed_books})