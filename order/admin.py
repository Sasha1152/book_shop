from django.contrib import admin

from .models import Order

# class SuborderInline(admin.TabularInline):
#     model = Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'total_price',
                    'is_returned',
                    'user_id',
                    )
    # inlines = [SuborderInline,]

admin.site.register(Order, OrderAdmin)
