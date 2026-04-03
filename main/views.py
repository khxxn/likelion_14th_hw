from django.shortcuts import render

def mainpage(request):
    return render(request,'main/mainpage.html')

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