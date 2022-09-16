from django.shortcuts import render, redirect
from myprofile.models import LanguageImage, Achievement
from myprofile.forms import ContactMsgForm
from django.utils import timezone

# Create your views here.



def loginpage(request):
    
    return render(request, 'login.html')
def index(request):
    return redirect('myprofile:index')



