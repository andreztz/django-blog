from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from django.urls import path


app_name = "core"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
]

