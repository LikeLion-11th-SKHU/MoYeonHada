from django.shortcuts import render
from .models import Bookmark

# Create your views here.

def base(request):
    return render(request, 'base.html')

def mypage(request):
    return render(request, 'mypage.html')

def bookmark(request):
    return render(request, 'bookmark.html')

def list(request):
    return render(request, 'list.html')



# def BookmarkList(ListView):
#     model = Bookmark

# def BookmarkCreate(CreateView):
#     model = Bookmark
#     fields = ['site_name', 'url', 'contents']
#     template_name_suffix = '_create'
#     success_url = '/'

# def BookmarkUpdate(UpdateView):
#     model = Bookmark
#     fields = ['site_name', 'url', 'contents']
#     template