from django.shortcuts import render

# Create your views here.
def loginpage(request):
    if request.method == "POST":
        
    else:
        return render(request, 'login.html')