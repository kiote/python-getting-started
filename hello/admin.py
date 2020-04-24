from django.contrib import admin
from hello.models import Message

# class MessageAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Message)
