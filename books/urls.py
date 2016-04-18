from django.conf.urls import url
from books.views import BookListView, BookDeleteView,\
    BookCreateView, BookUpdateView, BookCsvExporter


urlpatterns = [
    url(r'^list-books/$', BookListView.as_view(), name='book-list'),
    url(r'^delete-book/(?P<pk>\d+)$', BookDeleteView.as_view(), name='book-delete'),
    url(r'^add-book/$', BookCreateView.as_view(), name='add-book'),
    url(r'^update-book/(?P<pk>\d+)$', BookUpdateView.as_view(), name='book-update'),
    url(r'^export-books/$', BookCsvExporter.as_view(), name='book-exporter'),
]
