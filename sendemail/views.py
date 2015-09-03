from django.shortcuts import render
from django.core.mail import EmailMessage

import uuid

# Create your views here.
def send_email_with_uuid(email_address):
    key = uuid.uuid1()
    email = EmailMessage('Your Unique Key', "Here's your unique key:\n" + str(key), to=[email_address])
    return email.send()
