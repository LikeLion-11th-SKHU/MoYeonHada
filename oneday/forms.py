from django import forms
from .models import Oneday
from django.contrib.auth.forms import AuthenticationForm

class OnedayForm(forms.ModelForm):
    class Meta:
        model = OnedayRecruit
        fields = ['category', 'number', 'period', 'region', 'hashtag', 'title', 'content', 'picture']

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

        model = OnedayApply
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'phone_number', 'status', 'region_big', 'region_small', 'profile_image']

        labels = {
            'name': '이름',
            'phone': '전화번호',
            'number': '인원',
            'memo': '메모',
        }

        widgets = {
            'status': forms.RadioSelect(),
            'region_big': forms.Select(),
        }

class AuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
        ),
        'inactive': ("로그인 하세요."),
    }