import csv

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView,\
    CreateView
from django.core.urlresolvers import reverse_lazy
from books.models import Book
from django.http import HttpResponse, StreamingHttpResponse
# Create your views here.


class Echo(object):

    def write(self, value):
        return value


class BookListView(ListView):
    model = Book


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'num_pages', 'price', 'authors', 'is_read']
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

    
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'num_pages', 'price', 'authors', 'is_read',]
    success_url = reverse_lazy('book-list')


class BookCsvExporter(View):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        if books:
            rows = ([book.title, book.num_pages, book.price, 'Yes' if book.is_read else 'No'] for book in books)
            pseudo_buffer = Echo()
            writer = csv.writer(pseudo_buffer)
            response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                             content_type="text/csv")
            return response

        return HttpResponse("There are no books.")
