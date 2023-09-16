from django.shortcuts import render, reverse, redirect
from blog.models import Article
from django.contrib.auth.models import User
from django.views.generic import ArchiveIndexView, ListView



def home(request):
    articles = Article.objects.all()
    arts = articles.order_by('-created')[:3]
    return render(request, 'home_app/index.html',
                  {'articles': articles, 'recent_arts': arts})


class ArticleListLatestView(ListView):
    model = Article
    queryset = Article.objects.order_by('-created')[:2]
    template_name = 'home_app/index.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_banner']=Article.objects.order_by('-updated')[:4]
        return context



# def render_partial_view(request):
#     if request.path == reverse('home:sidebar_partial'):
#         return redirect('home:home')
#     recent_arts = Article.objects.order_by('-created')[:3]
#     updated_arts = Article.objects.order_by('-updated')[:3]
#     data = {'updated_arts': updated_arts, 'recent_arts': recent_arts}  # Another type of send variable to template.
#     return render(request, 'includes/sidebar.html', context=data)


def partial_view(request, pk):
    # if request.path == reverse('home:social_partial', args=[pk]):
    #     return redirect('home:home')
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'includes/social_media_share_.html', context=context)




