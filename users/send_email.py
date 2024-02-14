from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send(email):
    response = send_mail(
        subject="2meiget",
        message="Your ID has been fooud please come pick it up as soon as possible..",
        recipient_list=[email],
        from_email=settings.EMAIL_HOST_USER
    )
    return response

# postgresql://omoshjoe02:YZE8JHsDng1P@ep-blue-mud-a5i513b9.us-east-2.aws.neon.tech/tumeiget?sslmode=require