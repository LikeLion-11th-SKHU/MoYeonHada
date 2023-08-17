from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Teacher, TeacherComment


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['title', 'field', 'number', 'period1', 'period2', 'region', 'content', 'photo']
        exclude = ('user',)
        
        labels = {
            'title': '제목',
            'field': '모집 분야',
            'number': '모집 인원',
            'period1': '모집 기간1',
            'period2': '모집 기간2',
            'region': '진행 지역',
            'content': '모집 내용',
            'photo': '대표 사진',
        }
        
        widgets = {
            'field': forms.RadioSelect(),
            'period1': forms.DateInput(attrs={'type': 'date'}),
            'period2': forms.DateInput(attrs={'type': 'date'}),
            'content': SummernoteWidget(),
        }
    


class TeacherCommentForm(forms.ModelForm):
    class Meta:
        model = TeacherComment
        fields = ('content',)
        
        labels = {
            'content': ' ',
        }

