from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from blog_project import settings

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    # path('logout/', views.logout)
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('email/<int:pk>', views.EmailEditView.as_view(), name='email'),
    path('user_edit/<int:pk>', views.ProfileEditView.as_view(), name='user_edit')


]
