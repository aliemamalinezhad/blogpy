from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at,
            })
        context = {
            'article_data':article_data
        }

        return render(request, self.template_name, context)
