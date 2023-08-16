from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import OnedayCreate, OnedayApply, OnedayComment, OnedayReview, OnedayHashtag
from django.db import models


class OnedayCreateForm(forms.ModelForm):
    hashtag_input = forms.CharField(
        label='해시태그', 
        required=False, 
        help_text='해시태그를 쉼표로 구분해서 입력하세요',
        widget=forms.TextInput(attrs={'placeholder': '#예시'})
    )  # 새로운 필드 추가

    class Meta:
        model = OnedayCreate
        fields = ['title', 'field', 'number', 'period1', 'period2', 'region', 'content', 'photo']
        exclude = ('user', 'hashtags')

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

    def __init__(self, *args, **kwargs):
        super(OnedayCreateForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['hashtag_input'] = ', '.join([hashtag.tag for hashtag in self.instance.hashtags.all()])

    def save(self, *args, **kwargs):
        instance = super(OnedayCreateForm, self).save(commit=False)
        instance.save()

        # 기존 해시태그 연결 삭제
        instance.hashtags.clear()

        hashtag_names = self.cleaned_data['hashtag_input'].split(',')
        for name in hashtag_names:
            name = name.strip()
            if name.startswith("#"):
                name = name[1:]
            hashtag, created = OnedayHashtag.objects.get_or_create(tag=name)
            instance.hashtags.add(hashtag)
        return instance
    
class OnedayApplyForm(forms.ModelForm):
    class Meta:
        model = OnedayApply
        fields = ['name', 'phone', 'people', 'memo']
        exclude = ('user',)
        
        labels = {
            'name': '이름',
            'phone': '전화번호',
            'people': '지원 인원',
            'memo': '메모',
        }
        
        widgets = {
            'memo': SummernoteWidget(),
        }

class OnedayCommentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=OnedayComment.objects.all(),
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = OnedayComment 
        fields = ['content', 'parent']


class OnedayReviewForm(forms.ModelForm):
       class Meta:
        model = OnedayReview
        fields = ['content']