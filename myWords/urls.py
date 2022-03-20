from django.urls import path, include
from django.views.generic import RedirectView

from myWords.views import PostIndexView, DogPostsIndexView, CaretakerPostIndexView, \
    LitterPostIndexView, PostDetail

urlpatterns = [
    path('<int:id>', PostDetail.as_view(), name='post'),
    path('all', PostIndexView.as_view(), name='latestPosts'),
    path('all/<int:page>', PostIndexView.as_view(), name='posts'),
    path('litter', LitterPostIndexView.as_view(), name='latestLitterPosts'),
    path('litter/<int:page>', LitterPostIndexView.as_view(), name='litterPosts'),
    path('dog', DogPostsIndexView.as_view(), name='latestDogPosts'),
    path('dog/<int:page>', DogPostsIndexView.as_view(), name='dogPosts'),
    path('caretaker', CaretakerPostIndexView.as_view(), name='latestCaretakerPosts'),
    path('caretaker/<int:page>', CaretakerPostIndexView.as_view(), name='caretakerPosts'),
]
