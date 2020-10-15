from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated", "status")
    search_fields = ("title", "content")
    list_filter = ("created",)
    # raw_id_fields = ('tag',)
    date_hierarchy = "created"
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
