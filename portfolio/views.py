from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
#from django.core.mail import send_mail
from .models import *



def homepage(request):

    return render(request, 'portfolio/index.html')
