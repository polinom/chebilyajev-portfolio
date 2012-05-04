from django.contrib import admin
from models import ImageWork


class ImageWorkAdmin(admin.ModelAdmin):
    list_display=('title', 'updated','created')
    ordering = ('-created',)
    list_filter = ('image_type',)


admin.site.register(ImageWork, ImageWorkAdmin)