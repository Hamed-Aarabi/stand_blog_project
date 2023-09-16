from django.shortcuts import render
from django.views.generic import TemplateView

# def about(request):
#     return render(request, 'about_app/about.html')

class AboutView(TemplateView):
    template_name = 'about_app/about.html'