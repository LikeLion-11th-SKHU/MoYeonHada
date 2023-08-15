from django.shortcuts import render, redirect, get_object_or_404
from .models import OnedayCreate, OnedayApply, OnedayComment, Review, Hashtag
from .forms import OnedayCreateForm, OnedayApplyForm, OnedayCommentForm, ReviewForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.

def oneday_main(request):
    onedays = OnedayCreate.objects.all()

    # 검색 쿼리를 확인합니다.
    query = request.GET.get('q')
    if query:
        # 검색어에 따라 onedays 쿼리셋을 필터링합니다.
        onedays = onedays.filter(title__icontains=query)

    content = {'onedays': onedays}
    return render(request, 'oneday_main.html', content)

def oneday_create(request):
    if request.method == 'POST':
        form = OnedayCreateForm(request.POST, request.FILES)
        if form.is_valid():
            oneday = form.save(commit=False)
            oneday.user = request.user
            oneday.save()


        hashtag_text = request.POST.get('hashtag')  
        if hashtag_text:
            hashtags = hashtag_text.split()  
            for tag in hashtags:
                hashtag, created = Hashtag.objects.get_or_create(tag=tag)
                oneday.hashtags.add(hashtag)
        return redirect('oneday_read', pk=oneday.pk)

    else:
        form = OnedayCreateForm()

    content = {'form': form}
    return render(request, 'oneday_create.html', content)



def oneday_read(request, pk):
    oneday = get_object_or_404(OnedayCreate, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == oneday.user:
               oneday.delete()
               return redirect('oneday_main')
        return redirect('oneday_main')
    else:
        commentform = OnedayCommentForm()
        reviewform = ReviewForm()  # 리뷰 폼 추가
        comment = oneday.OnedayComments.all
        review = oneday.review_set.all

        content = {'oneday': oneday, 'commentform':commentform, 'comment':comment, 'reviewform':reviewform, 'review':review}
        return render(request, 'oneday_read.html', content)
    

def oneday_update(request, pk):
    oneday = OnedayCreate.objects.get(pk=pk)
    
    if request.user != oneday.user:
        return redirect('oneday_main')
    
    if request.method == 'POST':
        # 글 삭제 버튼이 눌렸을 경우
       if 'action' in request.POST and request.POST['action'] == '글 삭제':
            oneday.delete()
            return redirect('oneday_main')
       else:
            form = OnedayCreateForm(request.POST, request.FILES, instance=oneday)
            if form.is_valid():
                oneday = form.save(commit=False)

                hashtag_text = request.POST.get('hashtag')  # 이 부분을 추가
                if hashtag_text:
                    # 기존의 연결된 해시태그를 모두 지운다.
                    oneday.hashtags.clear()

                    hashtags = hashtag_text.split()  
                    for tag in hashtags:
                        hashtag, created = Hashtag.objects.get_or_create(tag=tag)
                        oneday.hashtags.add(hashtag)

                oneday.save()
                return redirect('oneday_read', pk=oneday.pk)
    else:
        form = OnedayCreateForm(instance=oneday)

    content = {'oneday': oneday, 'form': form, }
    return render(request, 'oneday_update.html', content)



def oneday_apply(request, pk):
    if request.method == 'POST':
        form = OnedayApplyForm(request.POST, request.FILES)
        if form.is_valid():
            apply_data = form.save(commit=False)
            apply_data.user = request.user
            apply_data.save()
            
            messages.success(request, '신청이 완료되었습니다!')
            return redirect('oneday_main')  # or some other page

    else:
        form = OnedayApplyForm()

    content = {'form': form}
    return render(request, 'oneday_apply.html', content)




def o_comment_create(request, pk):
    oneday = get_object_or_404(OnedayCreate, pk=pk)
    if request.method == 'POST':
        commentform = OnedayCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.oneday = oneday
            comment.user = request.user
            comment.save()
        return redirect('oneday_read', oneday.pk)

def o_comment_edit(request, comment_pk):
    comment = get_object_or_404(OnedayComment, pk=comment_pk)
    
    if request.user != comment.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        edited_content = request.POST.get('comment_content')
        
        if edited_content:  # 이 조건을 추가하여 edited_content가 비어있지 않을 경우에만 수정을 진행합니다.
            comment.content = edited_content
            comment.save()
        
        return redirect(reverse('oneday_read', kwargs={'pk': comment.oneday.pk}))

    return render(request, 'oneday_read.html', {'comment': comment})

def o_comment_delete(request, comment_pk):
    comment = OnedayComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        oneday_pk = comment.oneday_id  # 댓글이 연결된 oneday의 pk 값
        comment.delete()
    return redirect(reverse('oneday_read', kwargs={'pk': oneday_pk}))


def review_create(request, pk):
    oneday = get_object_or_404(OnedayCreate, pk=pk)
    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.oneday = oneday
            review.user = request.user
            review.save()
        return redirect('oneday_read', oneday.pk)

def review_edit(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.user != review.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        edited_content = request.POST.get('review_content')
        
        if edited_content:  # 이 조건을 추가하여 edited_content가 비어있지 않을 경우에만 수정을 진행합니다.
            review.content = edited_content
            review.save()
        
        return redirect(reverse('oneday_read', kwargs={'pk': review.oneday.pk}))

    return render(request, 'oneday_read.html', {'review': review})

def review_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        oneday_pk = review.oneday_id 
        review.delete()
    return redirect(reverse('oneday_read', kwargs={'pk': oneday_pk}))




def hashtag(request, hashtag=None):
    if hashtag:
        hashtag = get_object_or_404(Hashtag, tag=hashtag)
        onedays = OnedayCreate.objects.filter(hashtags=hashtag)
    else:
        onedays = OnedayCreate.objects.all()
    return render(request, 'hashtag.html', {'onedays': onedays})
    
def oneday_search(request):
    query = request.GET.get('query')  # 쿼리 문자열에서 검색어 추출
    search_results = []

    if query:
        # 제목에 검색어가 포함된 글들을 검색
        search_results = OnedayCreate.objects.filter(title__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 'oneday_search.html', context)