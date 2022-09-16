from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myprofile.models import Achievement, LanguageImage, ContactMessage
from myadmin.forms import LanguageInputForm, AchievementInputForm
# Create your views here.
@login_required(login_url ="common:loginpage")
def admin(request):
    #if(request.user != "admin"):
    #    return redirect("common:notallowedpage")
    #post, get 작업 분리
    context = dict()
    context['achievements'] = Achievement.objects.all().order_by('date')
    context['images'] = LanguageImage.objects.all()
    context['messages'] = ContactMessage.objects.all()
    return render(request, 'admin.html', context)
@login_required(login_url ="common:loginpage")
def addlang(request):
    if(str(request.user) != "admin" or request.method != "POST"):
        return redirect("common:notallowedpage")
    if(request.method == "POST"):
        form = LanguageInputForm(request.POST)
        if form.is_valid():
            lang = form.save(commit=False)
            lang.save()
        else:
            return redirect('common:notallowedpage')
        return redirect('myadmin:adminpage')
    else:
        return redirect('common:notallowedpage')
@login_required(login_url ="common:loginpage")
def addachiv(request):
    if(str(request.user) != "admin" or request.method != "POST"):
        return redirect("common:notallowedpage")
    if(request.method == "POST"):
        form = AchievementInputForm(request.POST)
        if form.is_valid():
            lang = form.save(commit=False)
            lang.save()
            
        else:
            print(form.errors)
            return redirect('common:notallowedpage')
        return redirect('myadmin:adminpage')
    else:
        return redirect('common:notallowedpage')
@login_required(login_url ="common:loginpage")
def deletelang(request, image_id):
    if(str(request.user) != "admin" or request.method != "POST"):
        return redirect("common:notallowedpage")
    image = LanguageImage.objects.get(id=image_id)
    image.delete()
    return redirect('myadmin:adminpage')
@login_required(login_url ="common:loginpage")
def deleteachiv(request, achiv_id):
    if(str(request.user) != "admin"):
        return redirect("common:notallowedpage")
    achiv = Achievement.objects.get(id=achiv_id)
    achiv.delete()
    return redirect('myadmin:adminpage')
@login_required(login_url ="common:loginpage")
def deletemsg(request, msg_id):
    if(str(request.user) != "admin"):
        print(request.user+" not equels admin")
        return redirect("common:notallowedpage")
    achiv = ContactMessage.objects.get(id=msg_id)
    achiv.delete()
    return redirect('myadmin:adminpage')

