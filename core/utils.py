import os
from decouple import config

from twilio.rest import Client

# account_sid = config('TWILIO_ACCOUNT_SID')
# auth_token = config('TWILIO_AUTH_TOKEN')

account_sid = 'AC0b871097667770740a4e87a1d5f774da'
auth_token = '2450449e9efab706f55244553754d298'
TWILIO_NUMBER = '+12567436566'


# Send sms via twillio when contact informantion is received from customers 
client = Client(account_sid, auth_token)


def send_sms(user_code, TWILIO_NUMBER):
    message = client.messages \
                    .create(
                        body=f"Hi! Your user and verification code is {user_code}",
                        from_=config('TWILIO_NUMBER'),
                        to=f'+2330208556743'
                    )

    print(message.sid)
