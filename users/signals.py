from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Searching,FoundId
from django.shortcuts import get_object_or_404 
from .send_email import send
from .send_sms import send_sms



@receiver(post_save,sender=FoundId)
def send_email_and_text(sender,**kwargs):
    if kwargs['created']: 
        try:
            search = Searching.objects.get(id_no=kwargs['instance'].id_no)
            print("sending message and email to :",search.email,search.phone)
            send(search.email)
            # send_sms(search.phone)
            
        except Searching.DoesNotExist:
            pass
