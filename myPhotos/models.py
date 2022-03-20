from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager

from myFriends.models import Caretaker
from myPaws.models import Dog, Litter, Puppy


class Photo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    source = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class DogPhoto(Photo):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class LitterPhoto(Photo):
    dog = models.ForeignKey(Litter, on_delete=models.CASCADE)


class PuppyPhoto(Photo):
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE)


class CaretakerPhoto(Photo):
    dog = models.ForeignKey(Caretaker, on_delete=models.CASCADE)