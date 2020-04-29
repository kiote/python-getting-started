from django.db import models

class Message(models.Model):
    created = models.DateTimeField("created", auto_now_add=True)
