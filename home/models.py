from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저 모델
class User(AbstractUser):
    email = models.EmailField(max_length = 255, unique = True, help_text = '주로 사용하는 이메일주소를 입력해주세요 ex) example@example.com')
    username = models.CharField(max_length = 200, null = False, blank = False, unique = True, help_text = '사용하실 아이디를 입력해주세요')
    nickname = models.CharField(max_length = 200, null = False, blank = False, help_text = '사용하실 별명을 입력해주세요')
    phone_number = models.CharField(max_length=200, null = False, blank = False, help_text = '핸드폰 주소를 입력해주세요')
    profile_image = models.ImageField(upload_to='images/', null = False, blank = True)

    status_CHOICES = (
        ('teacher', '선생님입니다'),
        ('student', '배우미입니다'),
    )
    status = models.CharField(max_length=20, choices=status_CHOICES, default='student')
    region_CHOICES = (
        ('서울', '서울'),
        ('경기도', '경기도'),
        ('강원도', '강원도'),
        ('충청도', '충청도'),
        ('전라도', '전라도'),
        ('경상도', '경상도'),
        ('인천', '인천'),
        ('대전', '대전'),
        ('광주', '광주'),
        ('대구', '대구'),
        ('울산', '울산'),
        ('부산', '부산'),
        ('제주', '제주'),
    )

    region_big = models.CharField(max_length=20, choices=region_CHOICES, default='student')
    region_small = models.CharField(max_length = 20, null = True, blank = True, help_text = '시 / 구 까지 작성해주세요', default='')
    region = models.CharField(max_length=20, default='서울시')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nickname']

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)

