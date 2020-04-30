from django.db import models

class Message(models.Model):
    created = models.DateTimeField("created", auto_now_add=True)
    sender_id = models.CharField(max_length=80, default="")
    token = models.CharField(max_length=200, default="")
    text = models.TextField(default="")
    raw_message = models.TextField(default="")
