from django.urls import path
from .views import get_members, create_member, contact_message_list

urlpatterns = [
    path('members/', get_members, name='get_members'),
    path('members/create/', create_member, name='create_member'),
    path('contact_messages/', contact_message_list, name='contact_message_list'),
]
