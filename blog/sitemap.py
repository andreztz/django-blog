from django.urls import reverse
from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSiteMap(Sitemap):

    changefreq = "daily"
    priority = 1

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class StaticSiteMap(Sitemap):

    changefreq = "weekly"
    priority = 0.5
    lastmod = None

    def items(self):
        return ["blog:about"]

    def location(self, item):
        return reverse(item)


class HomePageSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    location = "/"

    def items(self):
        return [self]

