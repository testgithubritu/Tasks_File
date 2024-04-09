from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Task_app.models import UserProfile, Education,link


# Create your views here.
def index(request):
    return render(request,'index.html')

def personal_details(request):

        profile=UserProfile.objects.all()
        obj=Education.objects.all()
        li=link.objects.all()

        return render(request,'index.html',{'profile':profile,'obj':obj,'li':li})





