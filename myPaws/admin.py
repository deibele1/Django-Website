from django.contrib import admin

from .models import OurDog, Litter, Puppy

admin.site.register(OurDog)
admin.site.register(Litter)
admin.site.register(Puppy)

