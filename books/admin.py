from django.contrib import admin
from books.models import Book, Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
