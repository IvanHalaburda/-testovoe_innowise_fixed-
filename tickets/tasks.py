from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@shared_task
def status_update_notification(title, email, new_status):
    """
    Sends author a notification about
    change in the status of his ticket
    """
    subject = 'Your ticket was updated'
    message = f'Status of your ticket "{title}" has changed to "{new_status}"'
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER,
              [recepient], fail_silently=False)
