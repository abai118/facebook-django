
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):

    return render(request, 'index.html')


def login(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(username)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,"invalid credentials")
            return redirect('/login')
        
    else :
        return render(request,'login.html')
    
    
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        
        if User.objects.filter(username = username).exists():
            messages.info(request, "username taken")
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, "email taken")
            return redirect('register')
        else :
            user = User.objects.create_user(username=username,password=password, email=email, first_name= firstname, last_name = lastname)
            print(user)
            # user.save()
            return redirect('login')
        
        
        
    return render(request, 'register.html')