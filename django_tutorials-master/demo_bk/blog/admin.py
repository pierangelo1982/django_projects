from django.contrib import admin
from .models import Post

class AdminDefault(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'pub_date', 'active', 'image_img']

admin.site.register(Post, PostAdmin)
