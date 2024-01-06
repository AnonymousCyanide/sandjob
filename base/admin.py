from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'subject')
    list_filter=['email']
    search_fields= ('name' , 'email' , 'subject')

admin.site.register(Message , MessageAdmin)
