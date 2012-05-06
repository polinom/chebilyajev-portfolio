from django.contrib import admin
from models import Galerry
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from models import Page

class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = Page


class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'image', 'bukvitsa')}),
    )

class GalerryAdmin(admin.ModelAdmin):
    list_display=('title', 'updated','created')
    ordering = ('-created',)
    list_filter = ('image_type',)


admin.site.unregister(FlatPage)
admin.site.register(Page, ExtendedFlatPageAdmin)
admin.site.register(Galerry, GalerryAdmin)