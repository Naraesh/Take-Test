from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Exam,Question

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

@login_required(login_url='/')
def candidate(request):
    obj=Exam.objects.all()
    return render(request,'student.html',{'con':obj})


@login_required(login_url='/')
def exadmin(request):
    con=Exam.objects.all()
    return render(request,'exadmin.html',{'con':con})

def canreg(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        mail = request.POST.get('email')
        password1 = request.POST.get('pwd1')
        password2 = request.POST.get('pwd2')
        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username exists')
                return redirect('register')
            elif User.objects.filter(email=mail):
                messages.warning(request, 'Email exists')
                return redirect('register')
            else:
                usr=User.objects.create_user(username=uname,email=mail,password=password1,is_active=False)
                return redirect('/')
        else:
            messages.warning(request,'password wrong')
            return redirect('register')

def log(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(username=uname,password=pwd)
        if user is not None:
            if user.is_active:
                if uname=='admin':
                    login(request,user)
                    return redirect('uadmin')
                else:
                    login(request,user)
                    return redirect('student')
        else:   
            return redirect('/')
    
def signout(request):
    logout(request)
    return redirect('/')
    

    
        