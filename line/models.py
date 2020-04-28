from django.db import models

class Message(models.Model):
    user = models.CharField("user", max_length=200)
    reply_token = models.CharField("reply_token", max_length=200)
    message = models.TextField("message")
    raw_message = models.TextField("raw_message")
