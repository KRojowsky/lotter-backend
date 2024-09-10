from django.urls import path
from .views import get_members, create_member, contact_message_list, check_member_status

urlpatterns = [
    path('members/', get_members, name='get_members'),
    path('members/create/', create_member, name='create_member'),
    path('members/status/', check_member_status, name='check_member_status'),
    path('contact_messages/', contact_message_list, name='contact_message_list'),
]
