from django.shortcuts import render
from django.views.generic import TemplateView

from myFriends.models import Caretaker
from myPaws.models import OurDog
from myPhotos.models import Photo
from myWords.models import Post


class CaretakerIndexView(TemplateView):
    caretakers = Caretaker.objects.all()
    template_name = 'myFriends/index.html'
    model = Caretaker

    def get_context_data(self, **kwargs):
        return {
            "friends": self.caretakers,
            "person": self.caretakers.order_by('?').first(),
            "caretakers": self.caretakers.order_by("dob")
        }


class CaretakerDetailView(TemplateView):
    context = {}
    template_name = 'myFriends/caretaker.html'
    model = Caretaker
    caretakers = Caretaker.objects.all()
    caretaker = None

    def get_caretaker(self, **kwargs):
        if self.caretaker is None:
            self.caretaker = self.caretakers.get(**kwargs)
        return self.caretaker

    def get_context_data(self, **kwargs):
        caretaker = self.get_caretaker(**kwargs)
        photos = Photo.objects.filter(tags__name__icontains=caretaker.first_name)
        posts = Post.objects.filter(poster=caretaker).order_by('-posting_time')[:5]
        dogs = OurDog.objects.all().filter(caretaker=caretaker)
        self.context['dogs'] = dogs
        self.context['posts'] = posts
        self.context['caretaker'] = self.caretaker
        self.context['caretakers'] = self.caretakers
        self.context['photos'] = photos
        return self.context
