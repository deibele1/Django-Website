from django.urls import path, include
from django.views.generic import RedirectView

from myFriends.views import CaretakerDetailView, CaretakerIndexView

urlpatterns = [
    path('index', CaretakerIndexView.as_view(), name='friend_index'),
    path('', RedirectView.as_view(url='/about/index', permanent=True)),
    path('<username>', CaretakerDetailView.as_view(), name='friend'),
]