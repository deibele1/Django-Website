from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from myFriends.models import Caretaker


class Sex(models.enums.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'


class Dog(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.MALE)
    description = models.CharField(max_length=1000)
    bio = RichTextUploadingField()
    birth_date = models.DateField('date of birth')
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    portrait = models.ImageField(upload_to='photos/dog_portraits/')

    def __str__(self):
        return self.name


class OurDog(Dog):
    pedigree = models.ImageField(upload_to='photos/pedigrees/')


class Litter(models.Model):
    mother = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='mother')
    father = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='father')
    photo = models.ImageField(upload_to='photos/litter_portraits')
    description = RichTextUploadingField()
    birth_date = models.DateField('date of birth')

    def __str__(self):
        return self.father.name + \
               " and " + \
               self.mother.name + \
               ': ' + \
               self.birth_date.__str__()


class Puppy(Dog):
    litter = models.ForeignKey(Litter, on_delete=models.CASCADE)
    pedigree = None

