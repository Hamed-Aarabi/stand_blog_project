from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path('', views.ArticelsListView.as_view(), name='blog'),
    path('detail/<slug:slug>', views.ArticlesDetailView.as_view(), name = 'blog_datail'),
    path('detail/<slug:slug>/addcomment', views.add_comment_article, name = 'blog_datail_commentadd'),
    path('postlike/<slug:slug>', views.like_article, name = 'blog_like'),
    path('postdislike/<slug:slug>', views.dislike_article, name = 'blog_dislike'),
    path('categorie/<int:pk>/', views.CategoriesListView.as_view(), name='categories_detail'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('tag/<str:tag>/', views.TagsListView.as_view(), name= 'tags'),
    path('user-articles/', views.UserArticlesView.as_view(), name= 'user_articles'),
    path('year/<int:year>/', views.ArticleYearArchiveView.as_view(), name= 'year_article'),
    path('add', views.AddArticleView.as_view(), name='article_add'),
    path('delete/<slug:slug>/', views.DeleteArticleView.as_view(), name= 'article_delete'),
    path('edit/<slug:slug>/', views.EditArticlesView.as_view(), name= 'article_edit'),




]