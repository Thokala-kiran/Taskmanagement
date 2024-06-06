from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'tasks': tasks, 'form': form}
    return render(request, 'home.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
        
    context = {'form': form}
    return render(request, 'update_task.html', context)

def deleteTask(request,pk):

    item = Task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context ={"item":item}
    return render(request, 'delete_task.html', context)

def registerTask(request):
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        username = request.POST["User_name"]
        password1 = request.POST["password"]
        password2 = request.POST["confirm_password"]
        if password1 == password2 :
            if User.objects.filter(username = username).exists():
                messages.info(request,'User Taken')
                return redirect('register')
                
            else :
                user= User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password1)
                user.save()
                print("user created")
                return redirect("login.html")
        else :
            print("password doesnt match")
            return redirect('register')
    return render(request,'register.html')
def loginTask(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password1 = request.POST["password"]
        user = auth.authenticate(username=username,password = password1)

        if user is not None :
            auth.login(request,user)
            return redirect("/")
        else :
            messages.info(request,"Invalid Credentials")
            return redirect('login.html')
    else :
        return render(request,'login.html')
    
def logoutTask(request):
    auth.logout(request)
    return redirect("/")

