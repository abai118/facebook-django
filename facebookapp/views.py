from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import profilemodel,Post
from django.contrib.auth import login ,logout,authenticate
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(profileuser__followers=request.user)
        friends = User.objects.filter()
        print(posts)
        return render(request, 'index.html',{'post':posts})
    else :
        return redirect('login')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(username)
        if user is not None:
            auth.login(request,user)
            print("ok")
            return redirect('/')
        else :
            messages.info(request,"invalid credentials")
            return redirect('login')

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
            userA = User.objects.create_user(username=username,
                                            password=password, email=email, first_name= firstname, last_name = lastname)
            print(userA)
            userA.save()
            if userA :
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request, user)
                    return redirect('updateProfile')
            # return render(request,'updateProfile.html')

    else :
        return render(request, 'register.html')

def logout(request):
    

    auth.logout(request)
    return redirect('login')

def updateProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bio = request.POST['bio']
            profilepic = request.FILES['profilepic']
            nickname = request.POST['nickname']
            profile = profilemodel.objects.create(user=request.user,image=profilepic,bio=bio,nickname=nickname)
            # profile.save()
            return redirect('profile')
        
        return render(request,'profileUpload.html')
    else :
        return redirect('login')
    
    

def profile(request):
    if request.user.is_authenticated:
        profile = profilemodel.objects.get(user=request.user)
        posts = Post.objects.filter(profileuser=profile)
        friends = profile.following
        print(friends)
        return render(request,'profile.html',{'profiles': profile,'posts':posts})
    else :
        return redirect('login')
    

def friends(request):
    if request.user.is_authenticated:
        profile = profilemodel.objects.all()
        print(profile)
        return render(request, 'friends.html')
    else :
        return redirect('login')
    
def notfound(request):
    return render(request, 'index.html')


def updatePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile = profilemodel.objects.get(user=request.user)
            
            
            
            postdesc = request.POST['desc']
            file = request.FILE['file']
            posts = Post.objects.create(postImg=file,profileuser=profile,user=request.user,text=postdesc)
            
            return render(request,'profile.html')
        else:
            messages.info(request, "something went wrong")
            return render(request,'uploadPost.html')
    else:
        return redirect('login')
            