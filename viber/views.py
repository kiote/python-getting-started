import json
import logging
import os
import requests

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)
viber_api_url = 'https://chatapi.viber.com/pa/'

from django.shortcuts import render

def callback_url(request):
    raw_message = request.body
    logger.error(raw_message)
    return HttpResponse('ok')
