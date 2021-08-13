from twilio.rest import Client
from core.settings import account_sid, auth_token, phone_number, twilio_number




# Send sms via twillio when contact informantion is received from customers 
client = Client(account_sid, auth_token)

def send_sms(user_code):
    message = client.messages \
                    .create(
                        body=f"Hi! Your user and verification code is {user_code}",
                        from_=twilio_number,
                        to=phone_number
                    )

    print(message.sid)
