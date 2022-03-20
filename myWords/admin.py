from django.contrib import admin

from .models import Post, LitterPost

admin.site.register(Post)
admin.site.register(LitterPost)