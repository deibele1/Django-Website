from django.core.paginator import Paginator
from django.views.generic import TemplateView

from myPhotos.models import Photo, DogPhoto, PuppyPhoto, CaretakerPhoto, LitterPhoto


class PhotoSearch(TemplateView):
    title = "All Photos"
    model = Photo
    template_name = 'myPhotos/search.html'
    page_size = 15

    def get_photos(self, **kwargs):
        return self.model.objects.all().filter(tags__name__in=kwargs['tags'].split("&")).order_by("-posted")

    def get_all_photos(self, **kwargs):
        return self.model.objects.all().order_by("-posted")

    def get_context_data(self, **kwargs):
        page = int(kwargs['page']) if 'page' in kwargs else 1
        next_page = page + 1
        tags = kwargs['tags'] if 'tags' in kwargs else 'all'
        all_photos = self.get_all_photos(**kwargs) if tags == 'all' else self.get_photos(**kwargs)
        paginator = Paginator(all_photos, 10)
        photos = paginator.page(page)
        more_photos = photos.has_next()
        last_page = page - 1
        return {"photos": photos,
                "page": page,
                "next_page": next_page,
                'tags': tags,
                'title': self.title,
                'more_photos': more_photos,
                'last_page': last_page}


class PhotoSearchEntry(PhotoSearch):
    template_name = 'myPhotos/search.html'
    title = "All Photos"

    def get_photos(self, **kwargs):
        return self.get_all_photos(**kwargs)


class DogPhotoSearch(PhotoSearch):
    title = "Dog Photos"
    model = DogPhoto


class PuppyPhotoSearch(PhotoSearch):
    title = "Puppy Photos"
    model = PuppyPhoto


class CaretakerPhotoSearch(PhotoSearch):
    title = "Caretaker Photos"
    model = CaretakerPhoto


class LitterPhotoSearch(PhotoSearch):
    title = "Litter Photos"
    model = LitterPhoto


class PhotoDetail(TemplateView):
    model = Photo
    template_name = 'myPhotos/photoDetail.html'

    def get_context_data(self, **kwargs):
        photo = self.model.objects.get(id=kwargs['id'])
        return {'photo': photo, 'tags': 'all'}
