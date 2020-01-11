from django.contrib import admin
from .models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name','desc','price')
    search_fields = ('name','desc')
    list_filter = ('name',)
admin.site.register(Destination, DestinationAdmin)
# Register your models here.
