import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

def message_callback(request):
    raw_message = request.body
    # d = json.loads(raw_message)
    # message_user = d['source']['userId']
    # message_reply_token = d['replyToken']
    # message_text = d['message']['text']

    # db_message = Message(user=message_user,
    #                      message=message_text,
    #                      raw_message=raw_message,
    #                      reply_token=message_reply_token)
    # db_message.save()

    logger.error(message_raw.decode("utf-8"))

    return HttpResponse('ok')
