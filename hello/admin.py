from django.contrib import admin
from hello.models import Message
from hello.models import Users

# class MessageAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Message)
admin.site.register(Users)
