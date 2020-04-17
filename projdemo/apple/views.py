from apple.tasks import send_email_task, sleepy
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # sleepy(10)
    sleepy.delay(10)
    return HttpResponse('Django: I\'m fine ;)')

def send_email(request):
    send_email_task()
    return HttpResponse('eMail has been sent!')