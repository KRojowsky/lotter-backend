from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'receipt', 'purchase_date')  # Dodaj nowe pole
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'receipt', 'purchase_date')  # Dodaj nowe pole do wyszukiwania
    ordering = ('-id',)

