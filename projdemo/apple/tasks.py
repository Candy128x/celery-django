from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None 


@shared_task
def send_email_task():
    sleepy(10)
    send_mail(
        'Kem che Bro W!', 
        'Test mail, celery - rabbitmq - django', 
        settings.EMAIL_HOST_USER, 
        ['sondagarashish@gmail.com'])

    return None