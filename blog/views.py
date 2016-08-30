from blog.models import Article
from blog.models import Tag
from blog.models import UserProfile

from django.contrib.syndication.views import Feed
from django.core import serializers
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse
# from django.http import JsonResponse

from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

def home(request):
    print(request.user)
    posts = get_list_or_404(Article, draft=False)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(
        request,
        'home.html',
        {'post_list': post_list}
    )


def serial(request):
    posts = get_list_or_404(Article, draft=False)
    return HttpResponse(
        serializers.serialize('json', posts),
        content_type="application/json"
    )


def about_me(request):
    context = {}
    description = UserProfile.objects.filter(pk=1).first()
    context['description'] = description
    return render(request, 'aboutme.html', context)


def detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    tags = get_list_or_404(Tag)
    return render(
        request,
        'post.html',
        {'post': post, 'tags': tags}
    )


def archives(request):
    post_list = get_list_or_404(Article, draft=False)
    return render(
        request,
        'archives.html',
        {'post_list': post_list, 'error': False}
    )


def search_tag(request, tag):
    post_list = get_list_or_404(
        Article.objects.filter(draft=False).filter(tag__tag_name__iexact=tag)
    )
    return render(request, 'tag.html', {'post_list': post_list})


def search_category(request, category):
    print(category)
    post_list = get_list_or_404(
        Article.objects.filter(draft=False).filter(category__iexact=category)
    )
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            return render(request, 'home.html')
    else:
        post_list = get_list_or_404(
            Article.objects.filter(title__icontains=search)
        )
        if len(post_list) == 0:
            return render(
                request,
                'archives.html',
                {'post_list': post_list, 'error': True}
            )
        else:
            return render(
                request,
                'archvies.html',
                {'post_list': post_list, 'error': False}
            )
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "/feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return get_list_or_404(
            Article.objects.filter(draft=False).order_by('-created_at')
        )

    def items_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created_at

    def item_description(self, item):
        return item.content
