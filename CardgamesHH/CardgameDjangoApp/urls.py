from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blackjack", views.blackjack, name="blackjack"),
    path("yablon", views.yablon, name="yablon"),
    path("war", views.war, name="war"),
]