from django.shortcuts import render, redirect, get_object_or_404
from .models import OnedayCreate, OnedayApply, OnedayComment, OnedayReview, OnedayHashtag
from .forms import OnedayCreateForm, OnedayApplyForm, OnedayCommentForm, OnedayReviewForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib import messages

from django.http import JsonResponse
from django.db.models import Count, Q


from mypage.models import WishlistOneday


# Create your views here.

def oneday_main(request):
    onedays = OnedayCreate.objects.all()
    
    # 사용되는 해시태그만 가져옵니다.
    all_hashtags = OnedayHashtag.objects.filter(~Q(tag = ''))
    all_hashtags = all_hashtags.annotate(num_onedays=Count('onedaycreate')).filter(Q(num_onedays__gt=0))
    
    # 검색 쿼리를 확인합니다.
    query = request.GET.get('q')
    if query:
        # 검색어에 따라 onedays 쿼리셋을 필터링합니다.
        onedays = onedays.filter(title__icontains=query)

    content = {
        'onedays': onedays,
        'all_hashtags': all_hashtags  # 템플릿으로 해시태그 전달
    }
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
                hashtag, created = OnedayHashtag.objects.get_or_create(tag=tag)
                oneday.hashtags.add(hashtag)
        else:
            hashtag_text = None
        return redirect('oneday_main')

    else:
        form = OnedayCreateForm()

    content = {'form': form}
    return render(request, 'oneday_create.html', content)



def oneday_read(request, pk):
    oneday = get_object_or_404(OnedayCreate, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == oneday.user:
                hashtags_in_oneday = oneday.hashtags.all()  # 해시태그 목록 가져오기
                oneday.delete()  # 게시글 삭제

                # 게시글에서 사용된 해시태그들 중 참조 횟수가 0인 해시태그 삭제
                for hashtag in hashtags_in_oneday:
                    if hashtag.onedaycreate_set.count() == 0:  # 해당 해시태그를 참조하는 게시글의 수 확인
                        hashtag.delete()

                return redirect('oneday_main')
        return redirect('oneday_main')
    else:
        commentform = OnedayCommentForm()
        reviewform = OnedayReviewForm()  # 리뷰 폼 추가
        comment = oneday.OnedayComments.all
        review = oneday.OnedayReviews.all

        content = {'oneday': oneday, 'commentform':commentform, 'comment':comment, 'reviewform':reviewform, 'review':review}
        if request.user.is_authenticated:
            # 여기서 'wishlist' 앱의 Wishlist 모델에 접근해서 찜 상태를 확인
            already_in_wishlist = WishlistOneday.objects.filter(user=request.user, o_post=oneday).exists()
            content['already_in_wishlist'] = already_in_wishlist
        return render(request, 'oneday_read.html', content)



    



def oneday_update(request, pk):
    oneday = get_object_or_404(OnedayCreate, pk=pk)
    
    # 권한 체크
    if request.user != oneday.user:
        messages.warning(request, "권한 없음")
        return redirect('oneday_main')
    
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == '글 삭제':
            hashtags_in_oneday = oneday.hashtags.all()  # 해당 글과 연결된 해시태그 목록 가져오기
            oneday.delete()  # 게시글 삭제

            # 게시글에서 사용된 해시태그들 중 참조 횟수가 0인 해시태그 삭제
            for hashtag in hashtags_in_oneday:
                if hashtag.onedaycreate_set.count() == 0:  # 해당 해시태그를 참조하는 게시글의 수 확인
                    hashtag.delete()

            return redirect('oneday_main')

        else:
            form = OnedayCreateForm(request.POST, request.FILES, instance=oneday)
            if form.is_valid():
                oneday = form.save(commit=False)
                
                hashtag_text = request.POST.get('hashtag')
                if hashtag_text:
                    # 기존의 연결된 해시태그를 모두 지운다.
                    oneday.hashtags.clear()

                    hashtags = hashtag_text.split()  
                    for tag in hashtags:
                        hashtag, created = OnedayHashtag.objects.get_or_create(tag=tag)
                        oneday.hashtags.add(hashtag)
                        
                oneday.save()
                return redirect('oneday_read', pk=oneday.pk)
    else:
        form = OnedayCreateForm(instance=oneday)

    content = {'oneday': oneday, 'form': form}
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

            # 대댓글 로직 추가
            parent_pk = request.POST.get('parent')
            if parent_pk:  # 대댓글인 경우
                parent_comment = OnedayComment.objects.get(pk=parent_pk)
                comment.parent = parent_comment

            comment.save()
        return redirect('oneday_read', oneday.pk)

def o_comment_edit(request, comment_pk):
    comment = get_object_or_404(OnedayComment, pk=comment_pk)

    # 권한 확인
    if request.user != comment.user:
        return JsonResponse({'status': 'fail', 'error': '권한 없음'})

    if request.method == "POST":
        new_content = request.POST.get('content')
        
        # 유효성 검사 추가
        if not new_content or len(new_content) == 0:
            return JsonResponse({'status': 'fail', 'error': '댓글 내용이 유효하지 않습니다.'})
        
        comment.content = new_content
        comment.save()
        return JsonResponse({'status': 'ok'})

def o_comment_delete(request, comment_pk):
    comment = OnedayComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        oneday_pk = comment.oneday_id  # 댓글이 연결된 oneday의 pk 값
        comment.delete()
    return redirect(reverse('oneday_read', kwargs={'pk': oneday_pk}))

def o_review_create(request, review_pk):
    oneday = get_object_or_404(OnedayCreate, pk=review_pk)
    if request.method == 'POST':
        reviewform = OnedayReviewForm(request.POST)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.oneday = oneday
            review.user = request.user
            review.save()
        # 리뷰 섹션을 보여주기 위해 URL에 ?view=reviews 파라미터 추가
        return redirect(reverse('oneday_read', kwargs={'pk': oneday.pk}) + '?view=reviews')
    
def o_review_edit(request, review_pk):
    review = get_object_or_404(OnedayReview, pk=review_pk)

    # 권한 확인
    if request.user != review.user:
        return JsonResponse({'status': 'fail', 'error': '권한 없음'})

    if request.method == "POST":
        new_content = request.POST.get('content')
        
        # 유효성 검사 추가
        if not new_content or len(new_content) == 0:
            return JsonResponse({'status': 'fail', 'error': '댓글 내용이 유효하지 않습니다.'})
        
        review.content = new_content
        review.save()
        return JsonResponse({'status': 'ok'})


def o_review_delete(request, review_pk):
    review = OnedayReview.objects.get(pk=review_pk)
    if request.user == review.user:
        oneday_pk = review.oneday_id  # 댓글이 연결된 oneday의 pk 값
        review.delete()
    # 리뷰 섹션을 보여주기 위해 URL에 ?view=reviews 파라미터 추가
    return redirect(reverse('oneday_read', kwargs={'pk': oneday_pk}) + '?view=reviews')




def o_hashtag(request, hashtag=None):
    if hashtag:
        hashtag = get_object_or_404(OnedayHashtag, tag=hashtag)
        onedays = OnedayCreate.objects.filter(hashtags=hashtag)
    else:
        onedays = OnedayCreate.objects.all()
    return render(request, 'hashtag.html', {'onedays': onedays})

def search_by_hashtag(request, hashtag):
    onedays_with_hashtag = OnedayCreate.objects.filter(hashtags__tag=hashtag)
    return render(request, 'oneday_main.html', {'onedays': onedays_with_hashtag})

def oneday_search(request):
    query = request.GET.get('query')  # 쿼리 문자열에서 검색어 추출
    search_results = []

    if query:
        # 제목에 검색어가 포함된 글들을 검색
        search_results = OnedayCreate.objects.filter(title__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 'oneday_search.html', context)