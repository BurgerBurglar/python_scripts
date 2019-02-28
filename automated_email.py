import smtplib
import time
from datetime import date, datetime

sender_name = "Shuo Tian"
sender_email = 'sxt173530@utdallas.edu'
server = smtplib.SMTP("smtpauth.utdallas.edu", 587)
password = "PASSWORD HERE"
receivers = {
             "Shuo Tian": 'tianshuo1996@outlook.com',
             "Chenyang Hu": "huchenyang.cheryl@gmail.com"
            }
interval_minutes = 0.1
subject = "Hi, I'm a Robot!"

message = """
My name is Scripty McScript, I work as an automated Python email sender.

You can configure the:

· sender name
· sender email
· receiver name
· receiver email
· subject
· message
· email frequency

and I'll send emails every X minutes/days/weeks... however you like!

Also, I can record the history of the emails and save them into a system log. So you can keep track of the emails - \
successes or failures - and view them whenever you want to!

Most importantly, I work for free!

Regards,
Scripty McScript
"""
body = """From: {} <{}>
To: {} <{}>
Subject: {}

Hi {}, 
{}

{}
"""


def login(sender, password):
    try:
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        print("Login success on {}".format(datetime.now()))
    except smtplib.SMTPException:
        print("Error: unable to login on {}".format(datetime.now()))


def send_email(sender, receiver, subject, body):

    receiver = receiver if isinstance(receiver, list) else [receiver]

    # Prepare actual message
    info = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender, ", ".join(receiver), subject, body)
    try:
        server.sendmail(sender, receiver, info)
        print("Successfully sent email to {} on {}".format(receiver[0], datetime.now()))
    except smtplib.SMTPException:
        print("Error: unable to send email to {} on {}".format(receiver[0], datetime.now()))


def timed_send_email(sender, password, mins, max_emails):

    login(sender, password)

    seconds = mins * 60
    for i in range(max_emails):
        for receiver_name, receiver_email in receivers.items():
            today = str(date.today())
            body_formated = body.format(sender_name
                                        , sender_email
                                        , receiver_name
                                        , receiver_email
                                        , subject
                                        , receiver_name.split(" ")[0]
                                        , message
                                        , today)
            send_email(sender_email, receiver_email, subject, body_formated)
        time.sleep(seconds)
    server.close()


timed_send_email(sender_email, password, interval_minutes, 1)
