from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.

def login(request):
	return render(request,'login1.html')