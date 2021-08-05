import os

from twilio.rest import Client

from django.db import models
from django.db.models.fields import CharField



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
        account_sid = 'AC0b871097667770740a4e87a1d5f774da'
        auth_token = '2450449e9efab706f55244553754d298'
        # client = Client(account_sid, auth_token)

        # message = client.messages \
        #                 .create(
        #                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        #                     from_='+12567436566',
        #                     to='+2330208556743'
        #                 )

        # print(message.sid)

        client = Client(account_sid, auth_token)
        notification = client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
            .notifications.create(
                to_binding='{"binding_type":"sms", "address":"+1651000000000"}',
                body='Knok-Knok! This is your first Notify SMS')
        print(notification.sid)


        return super().save(self, *args, **kwargs)