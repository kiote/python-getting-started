from django.db import models

class Message(models.Model):
    # created = models.IntegerField(default=0)
    sender_id = models.CharField(max_length=80, default="")
    token = models.CharField(max_length=200, default="")
    text = models.TextField(default="")
    raw_message = models.TextField(default="")
