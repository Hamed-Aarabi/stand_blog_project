from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', views.ArticleListLatestView.as_view(), name='home'),
    path('social-media/<int:pk>/', views.partial_view, name='social_partial'),
    # path('sidebar/', views.render_partial_view, name='sidebar_partial')



]
