from django.contrib import admin

# Register your models here.
from contacts.models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']

admin.site.register(Contacts, ContactsAdmin)