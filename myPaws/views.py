from django.shortcuts import render
from django.template import Context
from django.views.generic import TemplateView

# Create your views here.
from myPaws.models import Dog, Litter, Sex, Puppy, OurDog
from myPhotos.models import Photo
from myWords.models import Post


class DogIndexView(TemplateView):
    dogs = OurDog.objects.all()
    template_name = 'myPaws/index.html'
    model = OurDog

    def get_context_data(self, **kwargs):
        return {
            "dogs": self.dogs.all(),
            "dog": self.dogs.order_by('?').first(),
        }


class DogDetailView(TemplateView):
    dogs = OurDog.objects
    context = {}
    template_name = 'myPaws/dog.html'
    model = OurDog
    dog = None

    def get_dog(self, **kwargs):
        if self.dog is None:
            self.dog = self.dogs.get(**kwargs)
        return self.dog

    def get_litters(self, **kwargs):
        self.context['dogs'] = self.dogs.all()
        self.get_dog(**kwargs)
        return Litter.objects.filter(mother=self.dog) if self.dog.sex == 'F' else Litter.objects.filter(father=self.dog)

    def get_context_data(self, **kwargs):
        super(DogDetailView, self).get_context_data()
        dog = self.get_dog(**kwargs)
        photos = Photo.objects.filter(tags__name__icontains=dog.name)
        posts = Post.objects.filter(tags__name__icontains=dog.name)
        litters = self.get_litters(**kwargs)
        self.context['litters'] = litters
        self.context['posts'] = posts
        self.context['dog'] = self.dog
        self.context['photos'] = photos
        return self.context


class LitterIndexView(TemplateView):
    template_name = 'myPaws/litters.html'
    model = Litter

    def get_context_data(self, **kwargs):
        litters = self.model.objects.order_by('-birth_date')[:10]
        return {
            'litters': litters,
            'litter': litters.first()
        }


class LitterDetailView(TemplateView):
    template_name = 'myPaws/litter.html'
    model = Litter
    context = {}
    litters = Litter.objects.all()
    litter = None

    def get_litter(self, **kwargs):
        if self.litter is None:
            self.litter = self.litters.get(**kwargs)
        return self.litter

    def get_context_data(self, **kwargs):
        litter = self.get_litter(**kwargs)
        photos = litter.litterphoto_set.all()
        father = litter.father
        mother = litter.mother
        puppies = litter.puppy_set.all()
        self.context['litter'] = litter
        self.context['mother_litters'] = self.litters.filter(mother=mother)
        self.context['father_litters'] = self.litters.filter(father=father)
        self.context['father'] = father
        self.context['mother'] = mother
        self.context['puppies'] = puppies
        self.context['photos'] = photos
        return self.context


class PuppyDetailView(TemplateView):
    template_name = 'myPaws/puppy.html'
    model = Puppy
    context = {}
    puppies = Puppy.objects.all()
    puppy = None

    def get_puppy(self, **kwargs):
        if self.puppy is None:
            self.puppy = self.puppies.get(litter=kwargs['id'], name=kwargs['name'])
        return self.puppy

    def get_context_data(self, **kwargs):
        puppy = self.get_puppy(**kwargs)
        photos = puppy.puppyphoto_set.all()
        father = puppy.litter.father
        mother = puppy.litter.mother
        puppies = puppy.litter.puppy_set.all()
        self.context['puppy'] = puppy
        self.context['father'] = father
        self.context['mother'] = mother
        self.context['puppies'] = puppies
        self.context['photos'] = photos
        return self.context
