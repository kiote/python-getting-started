import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

logger = logging.getLogger(__name__)
line_api_url = 'https://api.line.me/v2/bot/message/reply'

def message_callback(request):
    raw_message = request.body
    d = json.loads(raw_message)
    for event in d['events']:
        if event['message']['type'] == 'text':
            logger.error(event)
            message_user = event['source']['userId']
            message_reply_token = event['replyToken']
            message_text = event['message']['text']
            db_message = Message(user=message_user,
                                 message=message_text,
                                 raw_message=raw_message,
                                 reply_token=message_reply_token)
            db_message.save()

    return HttpResponse('ok')

def message_repy(request):
    if exists():
        last_message = get_last_message()
        headers = {'content-type': 'application/json',
                   'authorization': 'Bearer %s' % os.environ.get('LINE_ACCESS_TOKEN')}
        payload = {'replyToken': last_message.reply_token, 'messages': [
            {'type': 'text', 'text': 'message1'},
            {'type': 'text', 'text': 'message2'}
        ]}
        r = requests.post(line_api_url, data=json.dumps(payload), headers=headers)
        print(r.text)
    else:
        logger.error('No messages')
    return HttpResponse('ok')

# private methods

def exists():
    Message.objects.count()

def get_last_message():
    Message.objects.all().order_by('-id')[:1][0]
