from django.contrib import admin
from .models import Book


class GenreInline(admin.TabularInline):
    model = Book.genre.through

class BookAdmin(admin.ModelAdmin):
    inlines = [
        GenreInline,
    ]
    exclude = ('genre',)
    list_display = ('id',
                    'title',
                    'author',
                    'year',
                    'pages',
                    'price',
                    'image',
                    'description',
                    )

admin.site.register(Book, BookAdmin)
