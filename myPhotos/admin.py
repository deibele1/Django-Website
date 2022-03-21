from django.contrib import admin

from .models import Photo, DogPhoto, LitterPhoto, PuppyPhoto, CaretakerPhoto

admin.site.register(Photo)
admin.site.register(DogPhoto)
admin.site.register(LitterPhoto)
admin.site.register(PuppyPhoto)
admin.site.register(CaretakerPhoto)
