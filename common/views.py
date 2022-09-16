from django.shortcuts import render, redirect
from myprofile.models import LanguageImage, Achievement, ContactMessage
from myprofile.forms import ContactMsgForm
from django.utils import timezone


# Create your views here.

def notallowed(request):
    return render(request, "invalidmethod.html")


