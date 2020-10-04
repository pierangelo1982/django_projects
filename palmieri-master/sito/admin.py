from django.contrib import admin
from sito.models import Post, Image, Allegato, Televisione, Curriculum, Galleria, Gallery, Video, Episodio, Folder, Galleriapagina, Galleriatelevisione
from image_cropping import ImageCroppingMixin
#rom django import forms

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Image)
admin.site.register(Allegato)
admin.site.register(Curriculum)
admin.site.register(Post, MyModelAdmin)
admin.site.register(Televisione, MyModelAdmin)
admin.site.register(Galleria, MyModelAdmin)
admin.site.register(Gallery, MyModelAdmin)
admin.site.register(Video, MyModelAdmin)
admin.site.register(Episodio, MyModelAdmin)
admin.site.register(Folder, MyModelAdmin)
admin.site.register(Galleriapagina, MyModelAdmin)
admin.site.register(Galleriatelevisione, MyModelAdmin)
