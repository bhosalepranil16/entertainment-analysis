from django.shortcuts import render
from django.views import View


from .models import BookModel
# Create your views here.


class BookDetail(View):
    def get(self, request, book_id):
        book = BookModel.objects.get(id=book_id)
        return render(request, 'books_section/book-detail.html', context={ "books_active": "active", "book_data": book })

class BookView(View):
    def get(self, request):
        return render(request, 'books_section/index.html', context={ "books_active": "active" })

    def post(self, request):
        book = request.POST['book']
        res = BookModel.objects.filter(title__icontains=book)
        return render(request, 'books_section/index.html', context={ "books_active": "active", "books_data": res })