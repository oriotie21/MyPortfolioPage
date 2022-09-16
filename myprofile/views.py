from django.shortcuts import render, redirect
from myprofile.models import LanguageImage, Achievement
from myprofile.forms import ContactMsgForm
from django.utils import timezone
import random

# Create your views here.


def index(request):
    context = {"images" : LanguageImage.objects.all(), "achievements" : Achievement.objects.all().order_by('date'),
    "cat_index" : get_cat_image_index(),
    }
    return render(request, "myprofile.html", context)
def get_cat_image_index():
    r = random.randrange(1,10)
    return r

def sendmsg(request):
    if request.method == 'GET':
        return render(request, "invalidmethod.html")
    elif request.method == 'POST':
        form = ContactMsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.date = timezone.now()
            msg.save()
        return redirect("/profile/")
    else:
        return render(request, "invalidmethod.html")



