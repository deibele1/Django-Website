from django.urls import path, include
from django.views.generic import RedirectView

from myPhotos.views import PhotoSearch, DogPhotoSearch, PuppyPhotoSearch, LitterPhotoSearch, CaretakerPhotoSearch, \
    PhotoDetail, PhotoSearchEntry

urlpatterns = [
    path('search/', PhotoSearchEntry.as_view(), name='photoSearch'),
    path('search/<tags>', PhotoSearch.as_view(), name='photoSearch'),
    path('search/<tags>/<int:page>', PhotoSearch.as_view()),
    path('search/dog/<tags>', DogPhotoSearch.as_view(), name='dogPhotoSearch'),
    path('search/dog/<tags>/<int:page>', DogPhotoSearch.as_view()),
    path('search/puppy/<tags>', PuppyPhotoSearch.as_view(), name='puppyPhotoSearch'),
    path('search/puppy/<tags>/<int:page>', PuppyPhotoSearch.as_view()),
    path('search/litter/<tags>', LitterPhotoSearch.as_view(), name='litterPhotoSearch'),
    path('search/litter/<tags>/<int:page>', LitterPhotoSearch.as_view()),
    path('search/caretaker/<tags>', CaretakerPhotoSearch.as_view(), name='caretakerPhotoSearch'),
    path('search/caretaker/<tags>/<int:page>', CaretakerPhotoSearch.as_view()),
    path('detail/<id>', PhotoDetail.as_view(), name='photoDetail'),
    path('', RedirectView.as_view(url='search/all', permanent=True))
]