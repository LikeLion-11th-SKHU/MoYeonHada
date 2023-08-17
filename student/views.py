from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, StudentComment
from .forms import StudentForm, StudentCommentForm
from django.urls import reverse
from mypage.models import WishlistStudent

# Create your views here.

def s_main(request):
    students = Student.objects.all()
    content = {'students':students}
    return render(request, 's_main.html', content)


@login_required
def s_c(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('s_r', pk=student.pk)
        
    else:
        form = StudentForm()
    content = {'form': form}
    return render(request, 's_c.html', content)



def s_r(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == student.user:
               student.delete()
               return redirect('s_main')
        return redirect('s_main')
    else:
        scommentform = StudentCommentForm()
        comment = student.StudentComments.all
        content = {'student': student, 'scommentform':scommentform, 'comment':comment}
        if request.user.is_authenticated:
            # 여기서 'wishlist' 앱의 Wishlist 모델에 접근해서 찜 상태를 확인
            already_in_wishlist = WishlistStudent.objects.filter(user=request.user, s_post=student).exists()
            content['already_in_wishlist'] = already_in_wishlist
        return render(request, 's_r.html', content)
    


def s_u(request, pk):
    student = Student.objects.get(pk=pk)
    if request.user != student.user:
        return redirect('s_main')
    if request.user == student.user:
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                return redirect('s_r', pk=student.pk)
        else:
            form = StudentForm(instance=student)
        content = {'student': student, 'form': form, }
        return render(request, 's_u.html', content)
    else:
        return redirect('s_main')


@login_required
def s_comment_create(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        scommentform = StudentCommentForm(request.POST)
        if scommentform.is_valid():
            comment = scommentform.save(commit=False)
            comment.student = student
            comment.user = request.user
            comment.save()
        return redirect('s_r', student.pk)


def s_comment_delete(request, comment_pk):
    comment = StudentComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        student_pk = comment.student_id  # 댓글이 연결된 teacher의 pk 값
        comment.delete()
    return redirect(reverse('s_r', kwargs={'pk': student_pk}))