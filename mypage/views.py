from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Wishlist, WishlistOneday
from .models import WishlistStudent
from django.db.models import Count

from teacher.models import Teacher
from student.models import Student
from oneday.models import OnedayCreate


#post
def t_post(request, t_post_id):
    t_post = get_object_or_404(Teacher, pk=t_post_id)
    context = {
        't_post': t_post,
    }
    if request.user.is_authenticated:
        already_in_wishlist = Wishlist.objects.filter(user=request.user, t_post=t_post).exists()
        context['already_in_wishlist'] = already_in_wishlist
    return render(request, 't_r.html', context)

def s_post(request, s_post_id):
    s_post = get_object_or_404(Student, pk=s_post_id)
    context = {
        's_post': s_post,
    }
    if request.user.is_authenticated:
        already_in_wishlist = WishlistStudent.objects.filter(user=request.user, s_post=s_post).exists()
        context['already_in_wishlist'] = already_in_wishlist
    return render(request, 's_r.html', context)

def o_post(request, o_post_id):
    o_post = get_object_or_404(OnedayCreate, pk=o_post_id)
    context = {
        'o_post': o_post,
    }
    if request.user.is_authenticated:
        already_in_wishlist = WishlistOneday.objects.filter(user=request.user, o_post=o_post).exists()
        context['already_in_wishlist'] = already_in_wishlist
    return render(request, 'o_r.html', context)
##################################################################
def my_posts_t(request):
    return render('my_posts_t.html')

def my_posts_s(request):
    return render('my_posts_s.html')

def my_posts_o(request):
    return render('my_posts_o.html')
#wishlist(t/s/o)#########################################################################333

def wishlist_t(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user).annotate(t_post_count=Count('t_post')).filter(t_post_count__gt=1)
    for wishlist_item in wishlists:
        duplicate_items = Wishlist.objects.filter(user=user, t_post=wishlist_item.t_post).order_by('id')[1:]
        for item in duplicate_items:
            item.delete()
    wishlists = Wishlist.objects.filter(user=user)
    return render(request, 'wishlist_t.html', {'wishlists': wishlists})

def wishlist_s(request):
    user = request.user
    wishlists_s = WishlistStudent.objects.filter(user=user).annotate(s_post_count=Count('s_post')).filter(s_post_count__gt=1)
    for wishlist_item in wishlists_s:
        duplicate_items = WishlistStudent.objects.filter(user=user, s_post=wishlist_item.s_post).order_by('id')[1:]
        for item in duplicate_items:
            item.delete()
    wishlists_s = WishlistStudent.objects.filter(user=user)
    return render(request, 'wishlist_s.html', {'wishlists_s': wishlists_s})

def wishlist_o(request):
    user = request.user
    wishlists_o = WishlistOneday.objects.filter(user=user).annotate(o_post_count=Count('o_post')).filter(o_post_count__gt=1)
    for wishlist_item in wishlists_o:
        duplicate_items = WishlistOneday.objects.filter(user=user, o_post=wishlist_item.o_post).order_by('id')[1:]
        for item in duplicate_items:
            item.delete()
    wishlists_o = WishlistOneday.objects.filter(user=user)
    return render(request, 'wishlist_o.html', {'wishlists_o': wishlists_o})

#add_to_wishlist ####################################################################
@login_required    
def add_to_wishlist_t(request, t_post_id):
    t_post = get_object_or_404(Teacher, pk=t_post_id)
    already_in_wishlist = Wishlist.objects.filter(user=request.user, t_post=t_post).exists()
    if not already_in_wishlist:
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, t_post=t_post)
    return redirect('wishlist_t')

@login_required  
def add_to_wishlist_s(request, s_post_id):
    s_post = get_object_or_404(Student, pk=s_post_id)
    already_in_wishlist = WishlistStudent.objects.filter(user=request.user, s_post=s_post).exists()
    if not already_in_wishlist:
        wishlist_item, created = WishlistStudent.objects.get_or_create(user=request.user, s_post=s_post)
    return redirect('wishlist_s')

@login_required  
def add_to_wishlist_o(request, o_post_id):
    o_post = get_object_or_404(OnedayCreate, pk=o_post_id)
    already_in_wishlist = WishlistOneday.objects.filter(user=request.user, o_post=o_post).exists()
    if not already_in_wishlist:
        wishlist_item, created = WishlistOneday.objects.get_or_create(user=request.user, o_post=o_post)
    return redirect('wishlist_o')


###########################################################################33
@login_required
def remove_from_wishlist_t(request, t_post_id):
    t_post = get_object_or_404(Teacher, pk=t_post_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, t_post=t_post)
    wishlist_item.delete()
    # messages.success(request, f"'{ t_post.title }'이/가 찜 목록에서 삭제되었습니다.")
    return redirect('wishlist_t')

@login_required
def remove_from_wishlist_s(request, s_post_id):
    s_post = get_object_or_404(Student, pk=s_post_id)
    wishlist_item = get_object_or_404(WishlistStudent, user=request.user, s_post=s_post)
    wishlist_item.delete()
    return redirect('wishlist_s')

@login_required
def remove_from_wishlist_o(request, o_post_id):
    o_post = get_object_or_404(OnedayCreate, pk=o_post_id)
    wishlist_item = get_object_or_404(WishlistOneday, user=request.user, o_post=o_post)
    wishlist_item.delete()
    return redirect('wishlist_o')

#내가 쓴글 보기(writing)####################################################################
def my_posts_t(request):
    posts_teacher = Teacher.objects.filter(user = request.user)
    return render(request, 'my_posts_t.html',{
        'posts_teacher':posts_teacher,
    }
                  )
def my_posts_s(request):
    posts_student = Student.objects.filter(user = request.user)
    return render(request, 'my_posts_s.html',{
        'posts_student':posts_student, 
    }
                    )
def my_posts_o(request):
    posts_oneday = OnedayCreate.objects.filter(user = request.user)
    return render(request, 'my_posts_o.html',{
        'posts_oneday':posts_oneday,
    }
                  )