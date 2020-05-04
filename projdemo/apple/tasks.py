from celery import shared_task
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None 


@shared_task
def send_email_task():
    # sleepy(10)
    for _ in range(5):
        send_mail(
            'Kem che Bro W! | TS:' + str(datetime.timestamp(datetime.now())), 
            'Test mail, celery - rabbitmq - django', 
            settings.EMAIL_HOST_USER, 
            ['sondagarashish@gmail.com'])

    return None