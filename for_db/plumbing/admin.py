from django.contrib import admin
from .models import Plumbing, PlumbingDetails

class PlumbingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'details')

class PlumbingDetailsAdmin(admin.ModelAdmin):
    list_display = ('plumbing', 'description')

admin.site.register(Plumbing, PlumbingAdmin)
admin.site.register(PlumbingDetails, PlumbingDetailsAdmin)