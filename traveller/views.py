from django.shortcuts import render
from datetime import datetime
from .models import Contactus
from django.contrib import messages
def home(request):
    return render(request, 'home.html')
def contactus(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Email = request.POST.get("Email")
        Desc = request.POST.get("Desc")
        contactus = Contactus(Username = Username, Email=Email, Desc=Desc, date= datetime.today())
        contactus.save()
        messages.success(request, 'Your message has been send')
    return render(request,'contactus.html')
