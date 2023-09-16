from django.db import models
import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE, max_length=50, verbose_name='نام')
    email = models.EmailField( verbose_name='ایمیل')
    subject = models.CharField(max_length=50, verbose_name='موضوع')
    body = models.TextField( verbose_name='پیام')
    recived_at = models.DateTimeField(default=datetime.datetime.now(), verbose_name='تاریخ دریافت')

    def __str__(self):
        return f'{self.name}--{self.subject}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'




class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_user', verbose_name='نام کاربر')
    subject = models.CharField(max_length=50, verbose_name='موضوع تیکت')
    ticket = models.TextField(verbose_name='متن تیکت')
    email = models.EmailField(verbose_name='ایمیل')
    recived_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

class TicketChild(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_admin', verbose_name='نام ادمبن')
    reply_to = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reply_ticket', verbose_name='جواب به', null=True)
    ticket_reply = models.TextField(verbose_name='متن جواب تیکت')
    send_at = models.DateTimeField(auto_now_add=True)