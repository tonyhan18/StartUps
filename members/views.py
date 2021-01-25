from django import template
from django.http import response
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Members
from django.template import Template,Context
# Create your views here.
def login(req):
    #print(dir(req))
    if(req.method=='GET'):
        return render(req,'login.html')
    elif(req.method=='POST'):
        #유저 email이 제대로 들어오지 않아도 표현은 된다.
        username = req.POST.get('username', None)
        useremail = req.POST.get('useremail', None)

        err = {}

        if not (useremail and username) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'login.html', err)
        else:
            member = Members.objects.get(username=username)

            if useremail == member.useremail:
                req.session['user']=member.id;
                return redirect('/members')
            else:
                err['err']="비밀번호가 잘못되었습니다."
                return render(req,"login.html",err)

            return HttpResponse(f"<h1>{member.useremail}<h1>")
            #return render(req, 'login.html', err)
    return redirect('/')

def login_after(req):
	# 아래 부분은 세션의 값을 직접 가지고 오는 것이다.
    user_id = req.session.get('user')
    if(user_id):
        return HttpResponse(f"로그인 유저 {user_id}")
    return HttpResponse("세션읽기 & 세션 없으면 리다이렉션")

def logout(req):
    if req.session.get('user'):
        del(req.session['user'])
    return redirect('/')


def result(request,port_num):
    response="You're looking t the result %s"
    # return HttpResponse(response % (port_num))
    return HttpResponse(response+f"{port_num}")



def gu(req):
    num = req.GET.get('num','')
    if(num==''): return HttpResponse('<h1> gugu : 0'+num_gugu(0) +'</h1>')
    else: return HttpResponse(f'<h1> gugu : {num}'+num_gugu(int(num)) +'</h1>')

def num_gugu(num):
    ans='<br>'
    for i in range(10):
        ans+=f'{num} x {i} = {num*i} <br>' 
    return ans

def index(request):
    context={"index_1":"코딩온","loop_1":range(10),"loop_2":range(10),"loop":(range(1,31)),}
    return render(request,'210121.html',context)

def signup(request):
    print(dir(request))
    if(request.method=='POST'):
        
        username=request.POST['username']
        email=request.POST['email']
        print(request.POST)
        #models의 class이다.
        member=Members(
                username=username,
                useremail=email
        )
        # 그냥 이렇게 하면 insert문이 실행된다.
        member.save()
        res_data={}
        res_data['res']='등록성공'
        print(res_data)

        return render(request,'login.html',res_data)
    return render(request, 'login.html')

def git(req):
    return HttpResponse("<h2>git version</h2>")
