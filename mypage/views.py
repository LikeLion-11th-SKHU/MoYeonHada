from django.shortcuts import render


# Create your views here.

def base(request):
    return render(request, 'base.html')

def mypage(request):
    return render(request, 'mypage.html')

def bookmark(request):
    return render(request, 'bookmark.html')

def list(request):
    return render(request, 'list.html')