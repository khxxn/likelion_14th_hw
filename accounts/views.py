from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Profile

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("main:postpage")
        else:
            return render(request, "accounts/login.html")
    elif request.method == "GET":
        return render(request, "accounts/login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("main:postpage")

def signup(request):
    if request.method == "POST":
        all_users = User.objects.all()

        for user in all_users: # 이미 존재하는 아이디인지 확인
            if user.username == request.POST['username']:
                return render(request, "accounts/signup.html", {'error': '이미 존재하는 아이디입니다.'})
        
        if request.POST['password'] == request.POST['password_confirm']:
            newuser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            nickname = request.POST['nickname']
            major = request.POST['major']
            insta = request.POST['insta']
            profile_image = request.FILES.get('profile_image')
            profile = Profile.objects.create(
                user=newuser,
                nickname=nickname,
                major=major,
                insta=insta,
                profile_image=profile_image,
            )
            auth.login(request, newuser)
            return redirect("main:postpage")
        else:
            return render(request, "accounts/signup.html", {'error': '비밀번호가 일치하지 않습니다.'})
        
    return render(request, "accounts/signup.html")