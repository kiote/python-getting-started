import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

logger = logging.getLogger(__name__)

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
