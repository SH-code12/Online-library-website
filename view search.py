from django.shortcuts import render
from .models import Books
from .forms import SearchForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def search(request):
    form = SearchForm()
    books = []

    if request.POST.get('query'):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books= Books.objects.filter(name__icontains=query) | Books.objects.filter(author__icontains=query) | Books.objects.filter(category__icontains=query)

    return render(request, 'registration/search.html', {'form': form, 'books': books})



