from django.conf.urls import url

from django.contrib.sitemaps.views import sitemap

from .sitemap import (
    ArticleSiteMap,
    StaticSiteMap,
    HomePageSiteMap,
)

sitemaps = {
    'article': ArticleSiteMap,
    'static': StaticSiteMap,
    'home': HomePageSiteMap,
}

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^serial/$', views.serial, name='serial'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutme/$', views.about_me, name='about_me'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^category/(?P<category>\w+)/$', views.search_category, name='search_category'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed/$', views.RSSFeed(), name='RSS'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitsitemap'),
]
