from django.urls import path, include
from django.views.generic import RedirectView

from myPaws.views import DogDetailView, LitterDetailView, PuppyDetailView, DogIndexView, LitterIndexView

urlpatterns = [
    path('', RedirectView.as_view(url='index', permanent=True)),
    path('index', DogIndexView.as_view(), name='bigPawIndex'),
    path('litters', LitterIndexView.as_view, name='littersIndex'),
    path('<name>', DogDetailView.as_view(), name='bigPaw'),
    path('littlePaws/<id>', LitterDetailView.as_view(), name='littlePaws'),
    path('littlePaws/<id>/<name>', PuppyDetailView.as_view(), name='littlePaw'),
]
