from django.db.models import Prefetch
from django.shortcuts import render

from articles.models import Article, ArticleTag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at').prefetch_related(
        Prefetch('scopes', ArticleTag.objects.order_by('-is_main', 'tag__name')))
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
