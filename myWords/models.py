from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from taggit.managers import TaggableManager

from myPaws.models import Litter, Dog
from myFriends.models import Caretaker


class Post(models.Model):
    posting_time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='posts/headline_image')
    poster = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
    tags = TaggableManager()

    def __str__(self):
        return self.title


class LitterPost(Post):
    litter = models.ForeignKey(Litter, on_delete=models.CASCADE)


class DogPost(Post):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class CaretakerPost(Post):
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
