from django.contrib import admin
from .models import Contact, Ticket, TicketChild



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ('recived_at', )


class TicketInLines(admin.TabularInline):
    model = TicketChild

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'ticket')
    list_filter = ('recived_at', 'user')
    inlines = [TicketInLines,]