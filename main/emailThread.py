from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import threading

class EmailThread(threading.Thread):

    def __init__(self, subject, body, from_email, recipient_list, fail_silently, image):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.image = image
        threading.Thread.__init__(self)


    def run(self):

        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)

        try:
            if self.image:
                # msg.attach_alternative(self.html, 'text/html')
                msg.attach(image.name, image.read(), image.content_type)
            msg.send(self.fail_silently)

        except:
            return "Attachment error"

        print("send email !!!")

def send_email(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):

    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()
