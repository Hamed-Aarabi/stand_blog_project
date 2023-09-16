from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Article, Categorie, Comment, Tags_For_Articles
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView, YearArchiveView
from django.urls import reverse_lazy, reverse
from .forms import AddArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MyLoginRequiredMIxin


# def blogs(request):
#     articles = Article.objects.all()
#     paginator = Paginator(articles, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog_app/blog.html', context={'page_obj': page_obj})


class ArticelsListView(ListView):
    model = Article
    template_name = 'blog_app/blog.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ArticelsListView, self).get_context_data(**kwargs)
        context['articles_count'] = Article.objects.all().count()
        return context


def blog_detail(request, slug):
    if request.user.is_authenticated == False:
        messages.error(request, 'For see article details login first.')
        return redirect('blog:blog')
    blog = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, user=request.user, article=blog, parent_id=parent_id)

    # blog.viewers += 1
    # blog.save()
    comments = blog.comments.filter(parent=None)
    paginator = Paginator(comments, 1)
    page_num = request.GET.get('page')
    comment_obj = paginator.get_page(page_num)
    return render(request, 'blog_app/post-details.html', context={'blog': blog, 'comment_obj': comment_obj})


class ArticlesDetailView(MyLoginRequiredMIxin, DetailView):
    model = Article
    context_object_name = 'blog'
    template_name = 'blog_app/post-details.html'

    def get(self, request, *args, **kwargs):
        blog = Article.objects.get(slug=self.kwargs.get('slug'))
        if not blog.viewers.filter(id=self.request.user.id).exists():
            blog.viewers.add(self.request.user.id)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data(**kwargs)
        blog = Article.objects.get(slug=self.kwargs.get('slug'))
        blog_comment = blog.comments.filter(parent=None)
        paginator = Paginator(blog_comment, 1)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['comment_obj'] = page_obj
        context['like_user'] = blog.like.filter(id=self.request.user.id).exists()
        context['dislike_user'] = blog.dislike.filter(id=self.request.user.id).exists()
        return context


def like_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.like.filter(id=request.user.id).exists():
        article.like.remove(request.user)
        return JsonResponse({'response': 'unliked'})
    else:
        article.like.add(request.user)
        if article.dislike.filter(id=request.user.id).exists():
            article.dislike.remove(request.user)
        return JsonResponse({'response': 'liked'})


def dislike_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.dislike.filter(id=request.user.id).exists():
        article.dislike.remove(request.user)
        return JsonResponse({'response': 'undislike'})
    else:
        article.dislike.add(request.user)
        if article.like.filter(id=request.user.id).exists():
            article.like.remove(request.user)
        return JsonResponse({'response': 'dislike'})


def add_comment_article(request, slug):
    if request.method == 'POST':
        msg = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(user=request.user, body=msg, parent_id=parent_id, article=Article.objects.get(slug=slug))
    return HttpResponseRedirect(reverse('blog:blog_datail', args=[slug]))


#
# class AddCommentView(MyLoginRequiredMIxin, FormView):
#     form_class = AddCommentForm
#     template_name = 'blog_app/add_commnet.html'
#     success_url = reverse_lazy('blog:blog')
#
#     def form_valid(self, form):
#         form_data = form.cleaned_data
#         blog = Article.objects.get(slug=self.kwargs.get('slug'))
#         Comment.objects.create(user=self.request.user, body=form_data['body'], parent_id=self.request.POST.get('parent_id'),
#                                article=blog)
#         return super().form_valid(form)


# def categories_detail(request, pk):
#     categorie = Categorie.objects.get(id=pk)
#     cat_title = categorie.name
#     articles = categorie.articles.all()
#     paginator = Paginator(articles, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog_app/blog.html', {'page_obj': page_obj, 'title': cat_title})


class CategoriesListView(ListView):
    model = Article
    template_name = 'blog_app/blog.html'
    paginate_by = 1

    def get_queryset(self, **kwargs):
        categories = Categorie.objects.get(id=self.kwargs.get('pk'))
        object_list = categories.articles.all()
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorie_in_url'] = Categorie.objects.get(id=self.kwargs.get('pk'))
        return context


#
# def search(request):
#     result = request.GET.get('q')
#     articles = Article.objects.filter(title__icontains=result)
#     title = f'search for {result}'
#     paginator = Paginator(articles, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog_app/blog.html', {'page_obj': page_obj, 'title': title})


class SearchListView(ListView):
    model = Article
    template_name = 'blog_app/blog.html'
    paginate_by = 1

    def get_queryset(self):
        result = self.request.GET.get('q')
        object_list = None
        if result:
            object_list = self.model.objects.filter(title__icontains=result)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = self.request.GET.get('q')
        return context


# def tags_of_articles(request, tag):
#     tags = get_object_or_404(Tags_For_Articles, tag_name=tag)
#     articles = tags.tag.all()
#     title = f'Result for articles contain of {tag} tag '
#     paginator = Paginator(articles, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog_app/blog.html', {'page_obj': page_obj, 'title': title})

class TagsListView(ListView):
    model = Article
    template_name = 'blog_app/blog.html'
    paginate_by = 1

    def get_queryset(self):
        tags = Tags_For_Articles.objects.get(tag_name=self.kwargs.get('tag'))
        object_list = tags.tag.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        context['tag_in_url'] = Tags_For_Articles.objects.get(tag_name=self.kwargs.get('tag'))
        return context


class UserArticlesView(ListView):
    model = Article
    template_name = 'blog_app/article_list.html'

    def get_queryset(self):
        object_list = Article.objects.filter(author__username=self.request.user.username)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_count'] = Article.objects.filter(author__username=self.request.user.username).count()
        return context


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog_app/article_delete.html'
    success_url = reverse_lazy('blog:user_articles')


class EditArticlesView(UpdateView):
    model = Article
    success_url = reverse_lazy('blog:user_articles')
    template_name = 'blog_app/article_edit.html'
    fields = ('title', 'image', 'body', 'author', 'tags', 'categorie', 'status')


#
# def add_article(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = AddArticleForm()
#     return render(request, 'blog_app/article_add.html', {'form': form})


class AddArticleView(CreateView):
    model = Article
    success_url = reverse_lazy('blog:user_articles')
    template_name = 'blog_app/article_add.html'
    fields = ('title', 'image', 'body', 'tags', 'categorie', 'status')

    def form_valid(self, form):
        form_data = form.save(commit=False)
        form_data.author = self.request.user
        form_data.save()
        return super().form_valid(form)


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = 'created'
    make_object_list = True
    paginate_by = 1
    template_name = 'blog_app/blog.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleYearArchiveView, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        return context
