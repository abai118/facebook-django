# from django.conf import messages
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
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            # message.info(request,"invalid credentials")
            return redirect('/login')
        
    else :
        return render(request,'login.html')