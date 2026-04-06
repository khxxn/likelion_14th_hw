from django.shortcuts import render

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
    return render(request,'main/mainpage.html', context)

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
    return render(request,'main/secondpage.html', context)