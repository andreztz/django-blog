from django.conf.urls import url
from django.urls import path

from . import views

app_name = "blog"


urlpatterns = [
    path("", views.home, name="home"),
    path("serial/", views.serial, name="serial"),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("archives/", views.archives, name="archives"),
    path("about/", views.about, name="about"),
    path("tag/<slug:tag>/<str:post>", views.search_tag, name="search_tag"),
    path(
        "category/<str:category>/",
        views.search_category,
        name="search_category",
    ),
    path("search/", views.blog_search, name="search"),
    path("feed/", views.RSSFeed(), name="RSS"),
]
