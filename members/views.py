from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def gu(req):
    num = req.GET.get('num','')
    if(num==''): return  HttpResponse('<h1> gugu : </h1>')
    else: return HttpResponse('<h1> gugu : '+num_gugu(int(num)) +'</h1>')

def num_gugu(num):
    ans='<br>'
    for i in range(10):
        ans+=f'{num} x {i} = {num*i} <br>' 
    return ans

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

def git(req):
    return HttpResponse("<h2>git version</h2>")
