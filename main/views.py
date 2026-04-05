from django.shortcuts import render

def mainpage(request):
    context = {
        'contents' : [
            ' 1. Django MTV 패턴',
            '2. View와 URL 연결',
            '3. Template Language',
            '4. Template 상속 및 포함',
            '5, 정적 파일'
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