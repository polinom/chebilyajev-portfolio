from django.contrib import admin
from models import Image
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from models import Page

class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = Page


class ExtendedFlatPageAdmin(FlatPageAdmin):
    list_display=('title', 'url',)
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'image', 'template_name')}),
    )

class ImageAdmin(admin.ModelAdmin):
    list_display=('picture', 'title','created')
    ordering = ('-created',)
    list_filter = ('gallery',)
    fieldsets = (
        (None, {'fields': ('image', 'gallery',)}),
    )


admin.site.unregister(FlatPage)
admin.site.register(Page, ExtendedFlatPageAdmin)
admin.site.register(Image, ImageAdmin)