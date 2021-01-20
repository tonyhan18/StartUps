from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def index(req):
    num=req.GET.get('num','')
    print(type(num))
    print(num)
    if len(num)<1:
        return HttpResponse('<h1> 파라미터가 없습니다. </h1>')
    if req.method=='GET':
        lotto=[]
        for i in range(6):
            num=random.randint(1,46)
            while(num in lotto):
                num=random.randint(1,46)
            lotto.append(random.randint(1,46))
        print(lotto)
        return HttpResponse(f"<h1>lotto 번호 추천 {lotto} </h1>")
    else:
        return HttpResponse("post")