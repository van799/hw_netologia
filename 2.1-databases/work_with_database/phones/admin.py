from django.contrib import admin

# Register your models here.
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'image',
        'release_date',
        'lte_exists',
        'slug'
    )

    list_filter = ('release_date', 'name')
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)
