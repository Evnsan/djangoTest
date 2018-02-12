from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy

from .forms.admin import BuildForm, ObservationAdminForm
from .models import Build, Picture, PhoneNumber, Owner, Feature, Observation,\
                    District

class ObservationInline(admin.StackedInline):
    model = Observation
    form = ObservationAdminForm
    extra = 1


class BuildAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'pub_date', 'project', 'address', 'tower', 'district',
            'availability', 'age', 'building_type', 'unit', 'face', 'empty',
            'selling_price', 'iptu', 'condominium_fee', 'square_meters',
            'units_per_floor', 'janitor_name', 'parking_slots', 'bedrooms',
            'bathrooms', 'suites', 'features', 'owners', 'pictures']})
    ]
    inlines = [ObservationInline]

admin.site.register(Build, BuildAdmin)

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1

class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['name']}),
        ('CONTATO',    {'fields': ['email']})
    ]
    inlines = [PhoneNumberInline]

admin.site.register(Owner, OwnerAdmin)

class PictureAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img heigth="100" width="100" src="{}" />'.format(obj.picture_file.url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag',]

admin.site.register(Picture, PictureAdmin)
admin.site.register(Feature)
admin.site.register(Observation)
admin.site.register(District)

admin.site.site_title = ugettext_lazy('Coecor admin')
# Text to put in each page's <h1> (and above login form).
admin.site.site_header = ugettext_lazy('Administração')
# Text to put at the top of the admin index page.
admin.site.index_title = ugettext_lazy('Administração do site')
