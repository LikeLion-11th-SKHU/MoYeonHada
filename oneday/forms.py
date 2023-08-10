from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import OnedayRecruit, OnedayApply

class OnedayRecruitForm(UserCreationForm):
    class Meta:
        model = OnedayRecruit
        fields = ['number', 'period', 'region', 'hashtag', 'title', 'content', 'picture']

        labels = {
            'category': '모집 분야',
            'number': '모집 인원',
            'period': '모집 기간',
            'region': '진행 지역',
            'hashtag': '해시태그',
            'title': '글 제목',
            'content': '모집 내용',
            'picture': '대표 사진',
        }

class OnedayApplyForm(UserCreationForm):
    class Meta:
        model = OnedayApply
        fields = ['username', 'phone_number', 'email', 'people', 'memo']

        labels = {
            'username': '이름', 
            '전화번호': '이메일',
            '인원': '비밀번호',
            '메모': '비밀번호 확인',
        }

        widgets = {
            'status': forms.RadioSelect(),
            'region_big': forms.Select(),
        }