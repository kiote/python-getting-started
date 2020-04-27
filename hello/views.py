import requests
import logging

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    telega_login = '<script async src="https://telegram.org/js/telegram-widget.js?8" data-telegram-login="GroundWorkerBot" data-size="large" data-auth-url="https://polar-plains-99906.herokuapp.com/" data-request-access="write"></script>'
    return HttpResponse('<pre>' + r.text + '</pre>' + telega_login)

def message(request):
    message = request.body
    logger.error(message.decode("utf-8"))
    return HttpResponse('<pre>' + message.decode("utf-8") + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
