from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from blog.sitemap import HomePageSiteMap
from blog.sitemap import PostSiteMap
from blog.sitemap import StaticSiteMap


app_name = "core"


sitemaps = {
    "posts": PostSiteMap,
    "static": StaticSiteMap,
    "home": HomePageSiteMap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitsitemap",
    ),
]
