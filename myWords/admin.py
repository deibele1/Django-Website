from django.contrib import admin


from .models import Post, LitterPost, DogPost, CaretakerPost


admin.site.register(Post)
admin.site.register(LitterPost)
admin.site.register(DogPost)
admin.site.register(CaretakerPost)
