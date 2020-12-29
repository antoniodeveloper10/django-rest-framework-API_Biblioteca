from django.contrib import admin
from books.models import Books

class Livros(admin.ModelAdmin):
    list_display = ('title', 'author', 'state')
    search_fields = ('author',)

admin.site.register(Books,Livros)