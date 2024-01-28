from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.show_entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_entry, name="random"),
    path("create", views.create_entry, name="create"),
    path("update/<str:entry_name>", views.update, name="update")
]
