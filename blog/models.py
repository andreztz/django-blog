from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.html import format_html

from . import meta
from .templatetags.markdownify import markdown

from simplemde.fields import SimpleMDEField
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status="draft")


class Post(models.Model):

    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=100)
    content = SimpleMDEField(blank=True, null=True)
    slug = models.SlugField("Slug")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default="draft"
    )

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    @property
    def summary(self):
        subs = '<a class="small" href="{}"> read more...</a>'.format(
            self.get_absolute_url()
        )

        metas, _ = meta.parse(self.content)
        if metas:
            metas["summary"] = metas["summary"][::-1].replace(
                "...", subs[::-1], 1
            )[::-1]
        return metas

    @property
    def body(self):
        _, content = meta.parse(self.content)
        return mark_safe(markdown(content))

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ["-created"]
