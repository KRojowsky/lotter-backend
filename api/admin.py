from django.contrib import admin
from .models import Member, ContactMessage

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'receipt')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'receipt')
    ordering = ('-id',)
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
