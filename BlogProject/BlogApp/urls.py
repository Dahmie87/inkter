from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>/", views.post_full, name="post-full"),
    path("create/", views.create, name="create"),
    path("ready/<int:post_id>/", views.ready, name="ready"),
]