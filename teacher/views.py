from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher

# Create your views here.
def t_main(request):
    return render(request, 't_main.html')

def t_c(request):
    return render(request, 't_c.html')

def t_create(request):
    teacher = Teacher()
    teacher.field = request.POST['field']
    teacher.number = request.POST['number']
    teacher.period1 = request.POST['period1']
    teacher.period2 = request.POST['period2']
    teacher.region = request.POST['region']
    teacher.title = request.POST['title']
    teacher.content = request.POST['content']
    teacher.photo = request.FILES['photo']
    teacher.save()
    return redirect('t_main')
    
def t_main(request):
    teachers = Teacher.objects.all()
    return render(request, 't_main.html', {'teachers': teachers})

def t_r(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 't_r.html', {'teacher': teacher})

def t_u(request, id):
    t_u = Teacher.objects.get(id = id)
    return render(request, 't_u.html', {'t_u': t_u})

def t_update(request, id):
    t_update = Teacher.objects.get(id=id)
    t_update.field = request.POST['field']
    t_update.number = request.POST['number']
    t_update.period1 = request.POST['period1']
    t_update.period2 = request.POST['period2']
    t_update.region = request.POST['region']
    t_update.title = request.POST['title']
    t_update.content = request.POST['content']
    t_update.photo = request.FILES['photo']
    t_update.save()
    return redirect('t_main')

def t_d(request, id):
    delete_diary = get_object_or_404(Teacher, id=id)
    delete_diary.delete()
    return redirect('t_main')