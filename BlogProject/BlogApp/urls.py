from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:ID>", views.postpage, name="post-full"),
    path("create", views.create, name="create")
]
