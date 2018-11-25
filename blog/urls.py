from django.conf.urls import url
from django.urls import path

from django.contrib.sitemaps.views import sitemap

from .sitemap import ArticleSiteMap, StaticSiteMap, HomePageSiteMap

app_name = "blog"

sitemaps = {
    "article": ArticleSiteMap,
    "static": StaticSiteMap,
    "home": HomePageSiteMap,
}

from . import views

# https://docs.djangoproject.com/en/2.1/ref/urls/
urlpatterns = [
    path("", views.home, name="home"),
    path("serial/", views.serial, name="serial"),
    url(r"^post/(?P<slug>[\w_-]+)/$", views.detail, name="detail"),
    path("archives/", views.archives, name="archives"),
    path("aboutme/", views.about_me, name="about_me"),
    url(r"^tag/(?P<tag>\w+)/$", views.search_tag, name="search_tag"),
    url(
        r"^category/(?P<category>\w+)/$",
        views.search_category,
        name="search_category",
    ),
    path(r"search/", views.blog_search, name="search"),
    path(r"feed/", views.RSSFeed(), name="RSS"),
    url(
        r"^sitemap\.xml$",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitsitemap",
    ),
]
