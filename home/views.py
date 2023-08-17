from django.shortcuts import render, redirect
from django.contrib import auth
from home.models import User
from .forms import UserForm, AuthenticationForm

from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
# from .forms import UserChangeForm
# from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required



# Create your views here.
# main.html
def main(request):
    return render(request, 'main.html')

# login.html
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')   
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

# logout.html
def logout(request):
    auth.logout(request)
    return redirect('main')

# signup.html
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            if user.region_small == None:
                user.region = user.region_big
            else:
                user.region = user.region_big + " " + user.region_small
            user.save()
            auth.login(request, user)
            return redirect('signup_end')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

# signup_end.html
def signup_end(request):
    return render(request, 'signup_end.html')

def main(request):
    return render(request, 'main.html')

# mypage.html
def mypage(request):
    return render(request, 'mypage.html')

def mypage_update(request):
    return render(request, 'mypage_update.html')

def delete(request):
    user = request.user #로그인 되어있는 user에 대한 정보를 가져오고
    user.delete()   #이 유저를 삭제
    logout(request) #해당 유저의 세션 정보 지우기

    #회원탈퇴할 때 진짜 할 것인지 한 번 더 물어보면 좋을 것 같음.
    return redirect('main')   #탈퇴 후 홈화면으로 redirect하기

# def mypage_profile(request):

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user) #instance에 현재 request에 있는 user의 정보 넣어줌
        if form.is_valid():
            form.save()
            # messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('mypage')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'mypage_update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password1')
            request.user.set_password(new_password)
            request.user.save()
            #비밀번호를 변경해도 로그아웃이 되지 않도록 함(세션 업데이트).
            update_session_auth_hash(request, form.user)
            # messages.success(request, '성공적으로 변경되었습니다.')
            return redirect('mypage')  # Replace 'profile' with the desired URL
    else:
        form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})
