from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def index(request):
    print(dir(request))
    return HttpResponse("hello")

def signup(request):
    if(request.method=='POST'):
        username=request.POST['username']
        email=request.POST['email']
        member=Members(
                username=username,
                useremail=email
        )
        member.save()
        res_data={}
        res_data['res']='등록성공'

        return render(request,'index.html',res_data)
    return render(request, 'index.html')

