from django.contrib import admin

# Register your models here.

from blog.models import Article
from blog.models import Tag
from blog.models import UserProfile
from blog.models import SocialMedia


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at','draft')
    search_fields = ('title', 'category', 'tag', 'content')
    list_filter = ('created_at',)
    # raw_id_fields = ('tag',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('social', 'url', 'link')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
