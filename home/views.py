from django.shortcuts import render, redirect
from django.contrib import auth
from home.models import User
from .forms import UserForm, AuthenticationForm

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