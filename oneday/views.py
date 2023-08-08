from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import OnedayApply, OnedayRecruit

# Create your views here.

def oneday_main(request):
    return render(request, 'oneday_main.html')

def oneday_new(request):
    return render(request, 'oneday_new.html')

def oneday_create(request):
    if request.method == 'POST':
        post = OnedayRecruit()
        post.title = request.POST['title']
        post.pub_date = timezone.now()
        post.body = request.POST['body']
        post.user = request.POST['user']
        post.mail = request.POST['mail']
        post.save()
        return redirect('oneday_read')
    return render(request, 'oneday_create.html')

def oneday_read(request):
    posts = OnedayRecruit.objects.all()
    return render(request, 'oneday_read.html', {'posts': posts})

def oneday_detail(request, id):
    post = get_object_or_404(OnedayRecruit, id=id)
    return render(request, 'oneday_detail.html', {'post': post})

def oneday_edit(request, id):
    edit_post = get_object_or_404(OnedayRecruit, id=id)
    return render(request, 'oneday_edit.html', {'edit_post': edit_post})

def oneday_update(request, id):
    update_post = get_object_or_404(OnedayRecruit, id=id)
    update_post.title = request.POST['title']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('oneday_read')

def oneday_delete(request, id):
    delete_post = get_object_or_404(OnedayRecruit, id=id)
    delete_post.delete()
    return redirect('oneday_read')