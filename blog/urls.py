from django.conf.urls import url
from django.urls import path

from . import views

app_name = "blog"


urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("archives/", views.archives, name="archives"),
    path("about/", views.about, name="about"),
    path(
        "tag/<slug:tag_slug>/<int:pk>/",
        views.similar_posts_by_tag,
        name="search_tag",
    ),
    path("search/", views.blog_search, name="search"),
    path("feed/", views.RSSFeed(), name="RSS"),
]
