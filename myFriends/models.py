from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Caretaker(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    dob = models.DateField()
    portrait = models.ImageField(upload_to='photos/caretaker_portraits/')
    phone = PhoneNumberField()
    email = models.EmailField(max_length=50)
    description = models.CharField(max_length=1000)
    bio = RichTextUploadingField()

    def __str__(self):
        return self.first_name + self.last_name
