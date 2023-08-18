# Generated by Django 4.2.3 on 2023-08-18 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnedayCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('period1', models.DateField(default='', max_length=50)),
                ('period2', models.DateField(default='', max_length=50)),
                ('region', models.CharField(default='', max_length=50)),
                ('field', models.CharField(choices=[('공예', '공예'), ('요리', '요리'), ('미술', '미술'), ('운동', '운동'), ('음악', '음악'), ('기타', '기타')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OnedayHashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OnedayReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('oneday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnedayReviews', to='oneday.onedaycreate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnedayReviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='onedaycreate',
            name='hashtags',
            field=models.ManyToManyField(to='oneday.onedayhashtag'),
        ),
        migrations.AddField(
            model_name='onedaycreate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OnedayComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('oneday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnedayComments', to='oneday.onedaycreate')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OnedayComments', to='oneday.onedaycomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnedayComments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnedayApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone1', models.PositiveIntegerField()),
                ('phone2', models.PositiveIntegerField(null=True)),
                ('phone3', models.PositiveIntegerField(null=True)),
                ('people', models.PositiveIntegerField()),
                ('memo', models.TextField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
