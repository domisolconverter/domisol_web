from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import threading
import os

class EmailThread(threading.Thread):

    def __init__(self, subject, body, from_email, recipient_list, fail_silently, path):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.path = path
        threading.Thread.__init__(self)


    def run(self):

        msg = EmailMessage(self.subject, self.body, self.from_email, self.recipient_list)

        try:
            if self.path:
                print("보낼준비여")
                msg.attach_file(self.path)

            msg.send(self.fail_silently)

        except:
            print("Attachment error")
            return "Attachment error"

        print("send email !!!")

def send_email(subject, body, from_email, recipient_list, fail_silently=False, path=None, *args, **kwargs):

    EmailThread(subject, body, from_email, recipient_list, fail_silently, path).start()
