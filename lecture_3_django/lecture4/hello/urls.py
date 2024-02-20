from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("veron", views.veron, name="veron"),
    path("<str:name>", views.greet, name="greet")


]
 