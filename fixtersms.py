from twilio.rest import Client
import time
import streamlit as st

# Twilio credentials
account_sid = 'ACb942bd73b4128c86649f710528454b2a'
auth_token = 'fca0c347814cedf4d7c1c329a92cb165'
twilio_number = '+12513131540'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to, body):
    message = client.messages.create(
        to=to,
        from_=twilio_number,
        body=body) 
    return message.sid

# Main function
def main(service_providers,address,title, issue):
    
    for provider in service_providers:
        # Send SMS to service provider
        body=f"Address: {address}\n Title: {title}\nIssue: {issue}\nNote: "
'''
        # Wait for 5 minutes for a response
        time.sleep(300)  # 300 seconds = 5 minutes
        
        # Check for response
        
        for message in client.messages.list():
            if message.direction == 'inbound' and message.from_ in service_providers:
                sender = message.from_
                response = message.body
                break
            else:
                sender = None
                response = None
        
        if response.lower() == "yes":
            break
        elif response == "no":
            message_sid = send_sms(provider, body)
            # Send the message to the next service provider
            continue
        else:
            body="The message has been withdrawn. thankyou"
            message_sid = send_sms(provider, body)
            # Send the message to the next service provider
            continue
'''