# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:33:07 2016

@author: Nachiket
"""
#send text message using phone

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "##########"
auth_token  = "#############"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="नमस्कार! हा मेसेज code करून पाठवलेला आहे!",
    to=["+17168168381","+919822388945","+919821592984"],    # Replace with your phone number
    from_="+17165174289") # Replace with your Twilio number
print message.sid
