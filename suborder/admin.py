from django.contrib import admin

from .models import Suborder


class SuborderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'quantity',
                    'is_returned',
                    'order_date',
                    'book_id',
                    'order_id',
                    )

admin.site.register(Suborder, SuborderAdmin)
