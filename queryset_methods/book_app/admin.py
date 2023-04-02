from django.contrib import admin
from .models import Author, Publisher, Book, Store, Item


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pages', 'price', 'rating', 'publisher', 'pubdate']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'data']
