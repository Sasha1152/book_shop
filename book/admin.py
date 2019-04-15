from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'author',
                    'title',
                    'year',
                    'pages',
                    'image',
                    'description',
                    )

admin.site.register(Book, BookAdmin)
