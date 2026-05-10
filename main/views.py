from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def mainpage(request):
    context = {
    'sections': [
        {
            'title': '🦁 목차',
            'items' : [
                '1. Django MTV 패턴',
                '2. View와 URL 연결',
                '3. Template Language',
                '4. Template 상속 및 포함',
                '5. 정적 파일 (Static Files)'
            ]
        },
        {
            'title': '🦁 1. Django MTV 패턴',
            'items': [
                'Model: 데이터의 정의 및 DB 조작을 담당함',
                'Template: 사용자에게 보여지는 HTML 화면을 구성함',
                'View: 요청에 따른 로직을 수행'
            ]
        },
        {
            'title': '🦁 2. View와 URL 연결',
            'items': [
                "View 작성: render(request, '경로/파일명.html', context)",
                "URL 설정: urls.py에서 path() 함수를 사용하여 특정 주소와 View 함수를 연결",
                "경로가 비어있는 ''은 유저가 처음 접속했을 때 보게 될 메인 페이지"
            ]
        },
        {
            'title': '🦁 3. Template Language',
            'items': [
                '변수: {{ name }} -> 구교현',
                '태그: {% for %}, {% if %} 반복문 조건문',
                '필터: {{ name | upper }}'
            ]
        },
        {
            'title': '🦁 4. Template 상속 및 포함',
            'items': [
                "상속: {% extends 'base.html' %}를 사용하여 공통 뼈대를 재사용함",
                "Block: 부모의 {% block %} 영역 안에 자식 페이지의 내용을 채워 넣음",
                "Include: {% include %}를 사용하여 네비바 등 반복되는 파일을 가져옴"
            ]
        },
        {
            'title': '🦁 5. 정적 파일 (Static Files)',
            'items': [
                'CSS, 이미지 등 변하지 않는 파일을 static 폴더에 모아 관리함',
                'HTML 최상단에 {% load static %}을 선언',
                'settings.py에서 STATICFILES_DIRS STATIC_ROOT 경로 설정'
            ]
        }
    ]
}
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {
        'info' : {
            'name': '구교현',
            'nickname': '구구콘 🍦',
            'mbti': 'ISTP',
            'hobby': '야구 시청 (LG 트윈스)',
            'insta': 'khxxn_9'
        }
    }
    return render(request, 'main/secondpage.html', context)

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'main/new_post.html')

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.content = request.POST['content']
    new_post.category = request.POST['category']

    new_post.save()
    save_tag(new_post)
    return redirect('main:detail', new_post.id)


def postpage(request):
    posts = Post.objects.all()
    return render(request,'main/postpage.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.GET.get('flag') == 'True':
        post.count += 1
        post.save()
        return redirect('main:detail', post_id)
        
    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        new_comments = Comment()

        new_comments.post = post
        new_comments.writer = request.user
        new_comments.content = request.POST['content']

        new_comments.save()
        return redirect('main:detail', post_id)
    
    comments = Comment.objects.filter(post=post)
    return render(request, 'main/detail.html', {'post': post, 'comments': comments})

def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id)

    if edit_post.writer != request.user:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {'post': edit_post})

def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    update_post = get_object_or_404(Post, pk=post_id)

    if update_post.writer != request.user:
        return redirect('main:detail', update_post.id)
    
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.content = request.POST['content']
    update_post.category = request.POST['category']
    update_post.save()

    save_tag(update_post)

    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_post = get_object_or_404(Post, pk=post_id)
    
    if delete_post.writer != request.user:
        return redirect('main:detail', delete_post.id)
    
    delete_post.delete()

    return redirect('main:postpage')

def comment_update(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    update_comment = get_object_or_404(Comment, pk=comment_id)
    post_id = update_comment.post.id

    if update_comment.writer != request.user:
        return redirect('main:detail', post_id)
    
    update_comment.writer = request.user
    update_comment.content = request.POST['content']
    update_comment.save()

    return redirect('main:detail', post_id)

def comment_delete(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_comment = get_object_or_404(Comment, pk=comment_id)
    post_id = delete_comment.post.id
    
    if delete_comment.writer != request.user:
        return redirect('main:detail', post_id)
    
    delete_comment.delete()
    return redirect('main:detail', post_id)

def save_tag(post):
    words = post.content.split()
    tag_list = []

    for w in words:
        if len(w) > 0:
            if w[0] == '#':
                tag_list.append(w[1:])

    post.tags.clear()

    for t in tag_list:
        tag, boolean = Tag.objects.get_or_create(name=t)
        post.tags.add(tag)

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html', {'tags': tags})

def tag_post_list(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag_post_list.html', {'tag': tag, 'posts': posts})