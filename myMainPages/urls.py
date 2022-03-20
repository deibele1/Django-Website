from django.urls import path

from myMainPages.views import MainView

urlpatterns = [
    path('<url>', MainView.as_view(), name='mainPage'),
    path('', MainView.as_view(), name='mainPage'),
]