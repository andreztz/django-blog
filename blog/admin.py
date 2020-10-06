from django.contrib import admin

# Register your models here.

from .models import Post
from .models import UserProfile
from .models import SocialMedia


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created", "updated", "status")
    search_fields = ("title", "category", "content")
    list_filter = ("created",)
    # raw_id_fields = ('tag',)
    date_hierarchy = "created"
    prepopulated_fields = {"slug": ("title",)}


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("social", "url", "link")


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
