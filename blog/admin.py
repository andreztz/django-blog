from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Tag
from .models import UserProfile
from .models import SocialMedia


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created", "updated", "status")
    search_fields = ("title", "category", "tag", "content")
    list_filter = ("created",)
    # raw_id_fields = ('tag',)
    date_hierarchy = "created"
    prepopulated_fields = {"slug": ("title",)}


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("social", "url", "link")


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "tag_name")


admin.site.register(Post, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
