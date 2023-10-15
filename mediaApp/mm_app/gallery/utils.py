
import json
from flask_mail import Message
from mediaApp.mm_app import mail


def send_contact_email(name, company, email, subject, users_message):
  token = ""
  msg = Message(subject,
                sender='noreply@demo.com',
                recipients=["eliruffin.tech@gmail.com"])
  msg.body = f'''
Name: 
{name}
Company: 
{company}
Message Content:
{users_message}

Supplied Email: 
{email}
'''
  mail.send(msg)
