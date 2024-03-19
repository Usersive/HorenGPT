from django.contrib import admin
from .models import ChatGPT
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class ChatGPTAdmin(admin.ModelAdmin):   
    list_display=('user', 'message', 'created_date')
    list_display_links=('user', 'message',)
    readonly_fields=('created_date',)
    ordering=('-created_date',)

admin.site.register(ChatGPT, ChatGPTAdmin)