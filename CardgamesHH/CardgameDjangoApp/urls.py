from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blackjack", views.blackjack, name="blackjack"),
    path("texasholdem", views.texasholdem, name="texasholdem"),
    path("war", views.war, name="war"),
]