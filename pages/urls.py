from re import template
from django.urls import path

from .views import HomePageView, AboutPageView, ProfilePageView
from accounts.views import ProfileUpdateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('profile/edit', ProfileUpdateView.as_view(), name="profile-update"),
]
