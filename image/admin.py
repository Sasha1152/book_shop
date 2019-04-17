from django.contrib import admin
from django.utils.html import format_html

from .models import Image


class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    image_tag.allow_tags = True

    list_display = ('id',
                'image',
                'image_tag',
                )

admin.site.register(Image, ImageAdmin)
