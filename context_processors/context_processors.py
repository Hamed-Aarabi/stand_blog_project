from blog.models import Article, Categorie, Tags_For_Articles
from django.shortcuts import reverse


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[:3]
    updated_articles = Article.objects.order_by('-updated')[:3]
    return {'recent_articles': recent_articles, 'updated_articles': updated_articles}


def categories(request):
    categories = Categorie.objects.all()
    return {'categories': categories}


# def urls(request):
#     home = reverse('home:home')
#     about = reverse('about:about')
#     blog = reverse('blog:blog')
#     contact = reverse('contact:contact')
#     return {'home': home, 'about': about, 'blog': blog, 'contact': contact}


def tag_of_articles(request):
    all_tags = Tags_For_Articles.objects.all()
    return {'all_tags':all_tags}


