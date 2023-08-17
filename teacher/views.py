from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Teacher, TeacherComment
from .forms import TeacherForm, TeacherCommentForm
from django.urls import reverse
from mypage.models import Wishlist

# Create your views here.

def t_main(request):
    teachers = Teacher.objects.all()
    content = {'teachers':teachers}
    return render(request, 't_main.html', content)


@login_required
def t_c(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('t_r', pk=teacher.pk)
        
    else:
        form = TeacherForm()
    content = {'form': form}
    return render(request, 't_c.html', content)



def t_r(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == teacher.user:
               teacher.delete()
               return redirect('t_main')
        return redirect('t_main')
    else:
        commentform = TeacherCommentForm()
        comment = teacher.TeacherComments.all
        content = {'teacher': teacher, 'commentform':commentform, 'comment':comment}
        if request.user.is_authenticated:
            # 여기서 'wishlist' 앱의 Wishlist 모델에 접근해서 찜 상태를 확인
            already_in_wishlist = Wishlist.objects.filter(user=request.user, t_post=teacher).exists()
            content['already_in_wishlist'] = already_in_wishlist
        return render(request, 't_r.html', content)
    


def t_u(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.user != teacher.user:
        return redirect('t_main')
    if request.user == teacher.user:
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('t_r', pk=teacher.pk)
        else:
            form = TeacherForm(instance=teacher)
        content = {'teacher': teacher, 'form': form, }
        return render(request, 't_u.html', content)
    else:
        return redirect('t_main')


@login_required
def t_comment_create(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        commentform = TeacherCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.teacher = teacher
            comment.user = request.user
            comment.save()
        return redirect('t_r', teacher.pk)


def t_comment_delete(request, comment_pk):
    comment = TeacherComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        teacher_pk = comment.teacher_id  # 댓글이 연결된 teacher의 pk 값
        comment.delete()
    return redirect(reverse('t_r', kwargs={'pk': teacher_pk}))