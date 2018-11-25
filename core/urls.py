from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

app_name = "core"

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include("blog.urls", namespace="blog")),
]