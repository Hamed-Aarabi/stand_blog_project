from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, RegisterForm, UserEditForm, ResetPasswordForm
from django.views.generic import CreateView, FormView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .mixins import MyAuthebticatedMixin


# def log_in(request):
#     if request.user.is_authenticated:
#         return redirect('home:home')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists() == False:
#             messages.error(request, 'username not found')
#             return redirect('accounts:login')
#         else:
#             user = authenticate(request, username=username, password=password)
#             if user is None:
#                 messages.error(request, 'password is incorrect.')
#                 return redirect('accounts:login')
#             else:
#                 login(request, user)
#                 return redirect('home:home')
#
#     return render(request, 'accounts/login.html', context={})

# def login_form(request):
#     if request.user.is_authenticated:
#         return redirect('home:home')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = User.objects.get(username=form.cleaned_data['username'])
#             login(request, user)
#             return redirect('home:home')
#     else:
#         form = LoginForm()
#
#     return render(request, 'accounts/login.html', {'form': form})

class LoginFormView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        user = User.objects.get(username=form.cleaned_data['username'])
        login(self.request, user)
        return super().form_valid(form)


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home:home')
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             obj_form = form.save(commit=False)
#             if form.cleaned_data['password'] == form.cleaned_data['re_password']:
#                 User.objects.create_user(username=obj_form.username, first_name=obj_form.first_name,
#                                          last_name=obj_form.last_name, email=obj_form.email,
#                                          password=form.cleaned_data['password'])
#                 return redirect('accounts:login')
#             else:
#                 messages.error(request, 'Passwords not match')
#                 return redirect('accounts:register')
#
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/signup.html', context={'form': form})

class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form_data = form.cleaned_data
        if form_data['password'] == form_data['re_password']:
            User.objects.create_user(username=form_data['username'], password=form_data['password'],
                                     email=form_data['email'], last_name=form_data['last_name'],
                                     first_name=form_data['first_name'])
        else:
            messages.error(self.request, 'Password not match bro')
            return redirect('accounts:register')
        return super().form_valid(form)



# def email_completion(request):
#     if request.user.is_authenticated == False:
#         return redirect('accounts:register')
#     if request.user.email:
#         return redirect('home:home')
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = User.objects.get(username=request.user.username)
#         user.email = email
#         user.save()
#         return redirect('contact:contact')
#
#     return render(request, 'accounts/email_comp.html')


class EmailEditView(MyAuthebticatedMixin,UpdateView):
    model = User
    template_name = 'accounts/email_comp.html'
    success_url = reverse_lazy('contact:contact')
    fields = ('email',)
    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated == False or self.request.user.email:
    #         return redirect('home:home')
    #     return super().get(request, *args, **kwargs)
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        self.request.user.email = email
        return super().form_valid(form)


# def profile_edit(request):
#     if request.user.is_anonymous:
#         return redirect('accounts:login')
#     form = UserEditForm(instance=request.user)
#     if request.method == 'POST':
#         form = UserEditForm(data=request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#     return render(request, 'accounts/edit_user.html', {'form':form})

class ProfileEditView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')
    template_name = 'accounts/edit_user.html'
    success_url = '/'



class ResetPasswordView(FormView):
    template_name = 'accounts/reset_password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form_obj = form.cleaned_data
        user = User.objects.get(username=form_obj['username'])
        user.set_password(form_obj['password'])
        user.save()
        return super().form_valid(form)
