import requests
import logging
import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message
from .models import Users

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    telega_login = '<script async src="https://telegram.org/js/telegram-widget.js?8" data-telegram-login="GroundWorkerBot" data-size="large" data-auth-url="https://polar-plains-99906.herokuapp.com/login" data-request-access="write"></script>'
    return HttpResponse('<pre>' + r.text + '</pre>' + telega_login)

def login(request):
    user_id = request.GET['id']
    if exists(user_id):
        pass
    else:
        user = Users(user=user_id)
        user.save()
    return HttpResponse('ok')

def message(request):
    message = request.body
    d = json.loads(message)

    message_text = d['message']['text']
    message_from = d['message']['from']['id']
    message_chat_id = d['message']['chat']['id']
    message_raw = message

    db_message = Message(user=message_from,
                         message=message_text,
                         raw_message=message_raw,
                         chat_id=message_chat_id)
    db_message.save()

    logger.error(message.decode("utf-8"))
    logger.error(d['message']['text'])
    return HttpResponse('<pre>' + message.decode("utf-8") + '</pre>')

def exists(user_id):
    Users.objects.filter(user=user_id).count()
