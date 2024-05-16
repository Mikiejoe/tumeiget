from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Searching,FoundId
from django.shortcuts import get_object_or_404 
from .send_email import send
from .send_sms import send_sms



@receiver(post_save,sender=FoundId)
def send_email_and_text(sender,**kwargs):
    print("sending email")
    if kwargs['created']: 
        try:
            search = Searching.objects.get(id_no=kwargs['instance'].id_no)
            print("sending message and email to :",search.email,search.phone,search.name,kwargs['instance'].station)
            send(search.email,search.name,kwargs['instance'].station.name)
            send_sms(search.phone,search.name,kwargs['instance'].station.name)
            
        except Searching.DoesNotExist:
            pass
    else:
        send(search.email,search.name,kwargs['instance'].station.name)
