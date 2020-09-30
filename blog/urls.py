from django.conf.urls import url
from django.urls import path

from django.contrib.sitemaps.views import sitemap

from .sitemap import ArticleSiteMap, StaticSiteMap, HomePageSiteMap

from . import views

app_name = "blog"

sitemaps = {
    "article": ArticleSiteMap,
    "static": StaticSiteMap,
    "home": HomePageSiteMap,
}


# https://docs.djangoproject.com/en/2.1/ref/urls/
urlpatterns = [
    path("", views.home, name="home"),
    path("serial/", views.serial, name="serial"),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("archives/", views.archives, name="archives"),
    path("aboutme/", views.about_me, name="about_me"),
    path("tag/<slug:tag>/<str:post>", views.search_tag, name="search_tag"),
    path(
        "category/<str:category>/",
        views.search_category,
        name="search_category",
    ),
    path("search/", views.blog_search, name="search"),
    path("feed/", views.RSSFeed(), name="RSS"),
    path(
        "sitemap\.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitsitemap",
    ),
]
