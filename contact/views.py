from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Contact, Ticket, TicketChild
from django.contrib import messages
from .forms import ContactForm
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# def contact(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             if request.user.email:
#                 name = request.POST.get('name')
#                 email = request.POST.get('email')
#                 subject = request.POST.get('subject')
#                 body = request.POST.get('message')
#                 if name and email and subject and body:
#                     Contact.objects.create(name=name, email=email, subject=subject, body=body)
#                     messages.success(request, f'Dear {name}, your message send successfully. Thank you')
#                     send_mail('Thank you', f'Dear {name}, Thank you for your ticket.', settings.EMAIL_HOST_USER,
#                               [email, ])
#                     return redirect('contact:contact')
#             else:
#                 messages.error(request, f'Dear {request.user.username}, you must fill email field to send ticket.')
#                 return redirect('accounts:email')
#         else:
#             messages.error(request, 'Dear user, you must register or login to site first.')
#             return redirect('accounts:register')
#
#     return render(request, 'contact_app/contact_form.html')


def contactus_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inc_form = form.save(commit=False)
            if request.user.is_authenticated:
                if request.user.email:
                    inc_form.save()
                else:
                    messages.error(request, 'You must fill email field for send tickets.')
                    return redirect('accounts:email')
            else:
                messages.error(request, 'You must fill login for send tickets.')
                return redirect('accounts:login')
    else:
        form = ContactForm()

    return render(request, 'contact_app/contact_form.html', {'form': form})


class ContactusView(FormView):
    template_name = 'contact_app/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Contact.objects.create(**form_data)
        return super().form_valid(form)


class MassagesView(CreateView):
    model = Contact
    fields = ('subject', 'body')
    success_url = reverse_lazy('contact:contact')
    template_name = 'contact_app/contact_form.html'

    def form_valid(self, form):
        form_object = form.save(commit=False)
        form_object.name = self.request.user
        form_object.email = self.request.user.email
        form_object.save()
        return super().form_valid(form)


class UserMessagesListView(ListView):
    model = Contact
    template_name = 'contact_app/contact_list.html'
    paginate_by = 2

    def get_queryset(self):
        object_list = Contact.objects.filter(name__username=self.request.user).order_by('-recived_at')
        return object_list


class UpdateMessagesView(UpdateView):
    model = Contact
    template_name = 'contact_app/contact_update.html'
    fields = ('subject', 'body')
    success_url = reverse_lazy('contact:users_messages')


class DeleteMessagesView(DeleteView):
    model = Contact
    template_name = 'contact_app/contact_delete.html'
    success_url = reverse_lazy('contact:users_messages')



class UserTicketsListview(ListView):
    model = Ticket
    template_name = 'contact_app/ticket_list.html'
    paginate_by = 2

    def get_queryset(self):
        object_list = Ticket.objects.filter(user__username=self.request.user).order_by('-recived_at')
        return object_list


class SendTicketView(CreateView):
    model = Ticket
    fields = ('subject', 'ticket')
    success_url = reverse_lazy('contact:tickets')
    template_name = 'contact_app/ticket_form.html'

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.user = self.request.user
        form_obj.email = self.request.user.email
        form_obj.save()
        return super().form_valid(form)

class TicketDetailview(DetailView):
    model = Ticket
    template_name = 'contact_app/ticket_detail.html'
    context_object_name = 'comment'

class DeleteTicketView(DeleteView):
    model = Ticket
    success_url = reverse_lazy('contact:tickets')
    template_name = 'contact_app/contact_delete.html'
