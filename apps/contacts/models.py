import os

from twilio.rest import Client

from django.db import models
from django.db.models.fields import CharField


from core.settings import account_sid, auth_token, phone_number, twilio_number



class Contact(models.Model):
    '''
    Contact information from our website
    '''
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    timestamp = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=254)


    def __str__(self):
        return f'{self.name}'

    
    def save(self, *args, **kwargs):
        
        # Send sms via twillio when contact informantion is received from customers
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Hi, Thank you for reaching.",
                            from_=twilio_number,
                            to=phone_number
                        )

        print(message.sid)


        return super().save(self, *args, **kwargs)