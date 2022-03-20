from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.db import models


class MainPage(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
    side_content = RichTextUploadingField()

    def __str__(self):
        return self.title
