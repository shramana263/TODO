from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.
def home(request,pk):
    user=account.objects.filter(pk__contains=pk)
    # print(user)
    tasks= Tasklist.objects.filter(username=User.objects.get(pk=pk)).order_by('-id')
    pending=Tasklist.objects.filter(username=User.objects.get(pk=pk),status="Incomplete")
    ptasks=pending.count()
    
    context={
        'tasks':tasks,
        'ptasks':ptasks
    }
    return render(request,"index.html",context)

def createtask(request,pk):
    user=User.objects.get(pk=pk)
    if request.method=="POST":
        title=request.POST['task_name']
        
        store=Tasklist(title=title,username=User.objects.get(pk=pk))
        store.save()
        
    return redirect('home',pk=user.pk)

def update(request,pk,pk1):
    
    # pk=self.kwargs.get('pk')
    
    task=Tasklist.objects.get(pk=pk)
    
    task.status="Completed"
    task.save()
    tasks= Tasklist.objects.filter(username=User.objects.get(pk=pk1)).order_by('-id')
    pending=Tasklist.objects.filter(username=User.objects.get(pk=pk1),status="Incomplete")
    ptasks=pending.count()
    context={
        'tasks':tasks,
        'ptasks':ptasks,
        # 'taskvar':taskvar,
    }
    return render(request,"index.html",context)
    
    
def delete_task(request,pk,pk1):
    task= Tasklist.objects.filter(username=User.objects.get(pk=pk1),pk=pk).order_by('-id')
    task.delete()
    tasks= Tasklist.objects.filter(username=User.objects.get(pk=pk1)).order_by('-id')
    pending=Tasklist.objects.filter(username=User.objects.get(pk=pk1),status="Incomplete")
    ptasks=pending.count()
    context={
        'tasks':tasks,
        'ptasks':ptasks,
    }
    return render(request,"index.html",context)

def completed_tasks(request,pk):
    tasks=Tasklist.objects.filter(username=User.objects.get(pk=pk),status="Completed").order_by('-id')
    context={
        'tasks':tasks,
    }
    return render(request,"completed_tasks.html",context)

def pending_tasks(request,pk):
    tasks=Tasklist.objects.filter(username=User.objects.get(pk=pk),status="Incomplete")
    context={
        'tasks':tasks,
    }
    return render(request,"pending_tasks.html",context)


def signup(request):
    
    if request.method=="POST":
        username = request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mobile']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        store= account(username=username, first_name=fname, last_name=lname, mobile=mobile, email=email)
        store.save()
        
        if User.objects.filter(username=username):
            messages.error(request,"username already exist!")
            return redirect('signup')
            
            
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('signup')
            
        if len(username)>20:
            messages.error(request,"Username must be under 20 characters.")
        
        if pass1 != pass2:
            messages.error(request,"Passwords didn't match")
            
        if not username.isalnum():
            messages.error(request,"Username must be alpha numeric")
            return redirect('signup')
        
        myuser= User.objects.create_user(username,email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        
        myuser.save()
        
        messages.success(request,"Your account has been created successfully")
        return redirect('signin')
    return render(request,"signup.html")


def signin(request):
    
    if request.method=='POST':
        username= request.POST['username']
        pass1= request.POST['pass1']
        
        user = authenticate(username= username, password= pass1) 
        if user is not None:
            login(request, user) 
            fname= user.first_name
            # print(user.pk)
            return redirect('home',pk=user.pk) 
        else:
            messages.error(request,"Bad Credntials!") 
            return redirect('signin')
    
    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out!")
    return redirect('signin')