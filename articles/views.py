from django.shortcuts import render

from articles.models import Article, Tag, TagScope


def articles_list(request):
    template = 'articles/news.html'

    context = {
        'object_list': Article.objects.all().order_by('-published_at')
    }

    return render(request, template, context)