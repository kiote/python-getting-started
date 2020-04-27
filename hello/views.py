import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Message
from .models import Users

from .forms import MessageForm

logger = logging.getLogger(__name__)
send_message_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s'

def index(request):
    return render(request, 'index.html')

def send_message(request):
    user_id = request.COOKIES['Telegram']
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            full_url = send_message_url % (os.environ.get('TELEGRAM_KEY'), user_id, message)
            r = requests.get(full_url)
            print(r.text)
            return HttpResponseRedirect('')
        else:
            print('Invalid form')

    return render(request, 'send_message.html', {'form': form})

def login(request):
    user_id = request.GET['id']
    response = HttpResponse('ok')
    if exists(user_id):
        response.set_cookie('Telegram', str(user_id))
    else:
        user = Users(user=user_id)
        user.save()
        response.set_cookie('Telegram', str(user_id))
    return response

# receiving messages from telegram here
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

## non-public stuff

def exists(user_id):
    Users.objects.filter(user=user_id).count()
