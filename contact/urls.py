from django.urls import path
from . import views

app_name= 'contact'
urlpatterns = [
    path('', views.MassagesView.as_view(), name = 'contact'),
    path('tickets/', views.UserTicketsListview.as_view(), name = 'tickets'),
    path('tickets/send', views.SendTicketView.as_view(), name = 'send_ticket'),
    path('tickets/<int:pk>', views.TicketDetailview.as_view(), name = 'ticket_detail'),
    path('tickets/delete/<int:pk>', views.DeleteTicketView.as_view(), name = 'delete_ticket'),
    path('messages/', views.UserMessagesListView.as_view(), name = 'users_messages'),
    path('update-msg/<int:pk>', views.UpdateMessagesView.as_view(), name = 'update_messages'),
    path('delet-msg/<int:pk>', views.DeleteMessagesView.as_view(), name = 'delete_messages'),

    ]