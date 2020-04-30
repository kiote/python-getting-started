import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message
from .forms import MessageForm

logger = logging.getLogger(__name__)
viber_api_url = 'https://chatapi.viber.com/pa/'

from django.shortcuts import render

def callback_url(request):
    raw_message = request.body
    logger.error(raw_message)
    d = json.loads(raw_message)
    if d['event'] == 'message':
        message_text = d['message']['text']
        message_token = d['message_token']
        sender_id = d['sender']['id']
        created = d['timestamp']
        db_message = Message(sender_id=sender_id,
                             token=message_token,
                             raw_message=raw_message,
                             text=message_text)
        db_message.save()
    return HttpResponse('ok')

def send_message(request):
    path = 'send_message'
    message_type = 'text'
    sender_name = 'MyBot'
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['user_id']
            full_url = viber_api_url + path
            headers = {'X-Viber-Auth-Token': os.environ.get('VIBER_ACCESS_TOKEN')}
            payload = {'receiver': receiver,
                       'type': message_type,
                       'sender_name': sender_name,
                       'text': message}
            r = requests.post(full_url, data=json.dumps(payload), headers=headers)
            print(r.text)
            return HttpResponseRedirect('')
        else:
            print('Invalid form')
    return render(request, 'send_message.html', {'form': form})


