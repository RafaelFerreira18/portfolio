from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    ...

admin.site.register(Message, MessageAdmin)
