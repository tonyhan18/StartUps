from django.shortcuts import render

# Create your views here.

def novel(req,char1="아나킨 스카이워커",char2="다스 시디어스"):
    context={"char1":char1,"char2":char2}
    return render(req,"novel.html",context)