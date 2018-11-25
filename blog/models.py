from django.db import models
from django.urls import reverse

# from django.core.urlresolvers import reverse
# from django.contrib.sites.models import Site

from django.utils.html import format_html
from django.contrib.auth.models import User

from simplemde.fields import SimpleMDEField


class UserProfile(models.Model):

    name = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to="profile_image", blank=True)
    description = SimpleMDEField(blank=True, null=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):

    social = models.CharField(max_length=100, blank=True)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "{}".format(self.social)

    @property
    def link(self):
        return format_html(
            '<a href="{}"  target="_blank">{}</a>', self.url, self.social
        )


class Tag(models.Model):

    tag_name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.tag_name)


class Article(models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = SimpleMDEField(blank=True, null=True)
    slug = models.SlugField("Slug")
    draft = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        # app_label = 'article'
        ordering = ["-created_at"]
