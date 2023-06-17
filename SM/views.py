from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from SM.models import experiments,Contactus

# Create your views here.
@login_required(login_url='login_page')
def home(request):
    sem3 = experiments.objects.filter(sem_num=3).count()
    sem4 = experiments.objects.filter(sem_num=4).count()
    sem5 = experiments.objects.filter(sem_num=5).count()
    sem6 = experiments.objects.filter(sem_num=6).count()
    sem7 = experiments.objects.filter(sem_num=7).count()
    sem8 = experiments.objects.filter(sem_num=8).count()
    params = {'sem3':sem3, 'sem4':sem4, 'sem5':sem5, 'sem6':sem6, 'sem7':sem7, 'sem8':sem8}
    return render(request,'index.html',params)

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone_no =request.POST.get('phoneno')
        age =request.POST.get('age')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.error(request, 'Password and Confrim Password must be same..')
            return redirect('registration')
        elif User.objects.filter(username=name):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('registration')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('registration')
        else:
            my_user=User.objects.create_user(name,email,pass1)
            my_user.save()
            return redirect('login_page')
    return render(request,'reg_page.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login_page')

def sem3(request):
    data = experiments.objects.filter(sem_num = 3)
    param = {"data":data}
    return render(request,'sem3.html',param)

def sem4(request):
    data = experiments.objects.filter(sem_num = 4)
    param = {"data":data}
    return render(request,'sem4.html',param)

def sem5(request):
    data = experiments.objects.filter(sem_num = 5)
    param = {"data":data}
    return render(request,'sem5.html',param)

def sem6(request):
    data = experiments.objects.filter(sem_num = 6)
    param = {"data":data}
    return render(request,'sem6.html',param)

def sem7(request):
    data = experiments.objects.filter(sem_num = 7)
    param = {"data":data}
    return render(request,'sem7.html',param)

def sem8(request):
    data = experiments.objects.filter(sem_num = 8)
    param = {"data":data}
    return render(request,'sem8.html',param)

def additem(request):
    if request.method == "POST":
        expname = request.POST.get('expt_name')
        subname = request.POST.get('subject')
        semnum = request.POST.get('semnum')
        expfile = request.FILES["expt_file"]
        data = experiments(exp_name = expname,subject_name = subname, sem_num = semnum, exp_file = expfile )
        data.save()
    return render(request,'additem.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        data = Contactus(name = fname, email = email, msg = msg)
        data.save()
    return render(request,'contact.html')
