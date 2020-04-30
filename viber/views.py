import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

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
        db_message = Message(created=created,
                             sender_id=sender_id,
                             token=message_token,
                             raw_message=raw_message,
                             text=message_text,
                            )
        db_message.save()
    return HttpResponse('ok')
