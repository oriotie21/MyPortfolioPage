from django.shortcuts import render, redirect
from myprofile.models import LanguageImage, Achievement
from myprofile.forms import ContactMsgForm
from django.utils import timezone

# Create your views here.


def index(request):
    context = {"images" : LanguageImage.objects.all(), "achievements" : Achievement.objects.all()}
    return render(request, "test.html", context)
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








