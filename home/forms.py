from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label = '비밀번호', widget = forms.PasswordInput)
    password2 = forms.CharField(label = '비밀번호 재확인', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'phone_number', 'status', 'region_big', 'region_small', 'profile_image']

        labels = {
            'username': '아이디',
            'email': '이메일주소',
            'password1': '비밀번호',
            'password2': '비밀번호 재확인',
            'nickname': '별명',
            'phone_number': '전화번호',
            'profile_image': '프로필 사진',
            'status': '가입 목적',
            'region_big': '도 / 시',
            'region_small': '시 / 구',
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
        'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
    }