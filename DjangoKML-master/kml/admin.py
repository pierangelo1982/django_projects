from django.contrib import admin
from kml.models import *


# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    pass

class PathAdmin(admin.ModelAdmin):
    list_display = ("titolo", "marker", "mappa", "mykml")

admin.site.register(Path, PathAdmin)
