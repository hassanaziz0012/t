from django.contrib import admin

from core.models import StaticImage

# Register your models here.
@admin.register(StaticImage)
class StaticImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    