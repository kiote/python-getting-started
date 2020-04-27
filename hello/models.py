from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Message(models.Model):
    user = models.CharField("user", max_length=80)
    message = models.TextField("message")
    raw_message = models.TextField("raw_message")
