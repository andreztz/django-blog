from django.urls import reverse
from django.contrib.sitemaps import Sitemap

from .models import Post


class ArticleSiteMap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticSiteMap(Sitemap):

    lastmod = None
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["about_me"]

    def location(self, item):
        return reverse(item)


class HomePageSiteMap(Sitemap):
    location = "/"
    changefreq = "daily"
    priority = 1

    def items(self):
        return [self]

    #
    # def lastmod(self, obj):
    #     return datetime.date.today()
    #
    # def location(self, item):
    #     return reverse(item)
