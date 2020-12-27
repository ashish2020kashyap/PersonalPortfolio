from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
#from django.core.mail import send_mail
from .models import Contact



def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact= Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        subjects="Thank you for visiting to our site"
        messages="We will contact you soon............"
        send_mail(subjects, messages, email_from, recipient_list)

    return render(request, 'port/index.html')

