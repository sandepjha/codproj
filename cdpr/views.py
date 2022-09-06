
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUp
from django.contrib.auth import authenticate, login, logout
from .models import Register
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import LoginForm
# Create your views here.


def base(request):
    return render(request,"base.html")

def Signup(request):
    if request.method == 'POST':
        fms = SignUp(request.POST)
        if fms.is_valid():
            fms.save()
            return HttpResponseRedirect('/login')
    else:
        fms= SignUp()
    return render(request,"signup.html", {'fm':fms})

# def Login(request):
#     if request.method=="POST":
#         mobile = request.POST['name']
#         password = request.POST['pass']
#         user = authenticate(username=mobile,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/social")
#     else:
#         return render(request,"login.html")


def Login(request):
    if request.method == "POST":
        fm = LoginForm(request.POST)
        # mobile = fm.cleaned_data['mobile']
        # password = fm.cleaned_data['password']
        mobile = request.POST['mobile']
        password = request.POST['password']
        user = authenticate(mobile=mobile, password =password)
        if fm.is_valid():
            # login(request, user)
            return redirect('/social')
    else:
        fm = LoginForm()
        return render(request, "login.html", {'form':fm})

def home(request):
    return render(request,"home.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect("login")