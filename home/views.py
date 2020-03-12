from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate
from .form import *
from .models import *
import requests
import json
# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")
#board
def board(request):
    return render(request,"board.html")
#member
def signout(request):
    if request.session.get('myid') is not None:
        del request.session['myid']
    return render(request,"home.html")
def signup(request):
    if request.method=='POST':
        form=Createsignup(request.POST)
        if form.is_valid():
            #아이디에 들어가는 전체폼을 완성시키겠다?
            #new_user=User.objects.create_user(**form.cleaned_data)
            #Member.objects.create(form_cleaned_data)  도 가능할듯??
            member=Member.objects.create(**form.cleaned_data)
            member.save()
            #form.save() 도 가능함.
            print("save 완료")
            return redirect('signin')
        else:
            return redirect('signup')
    else:
        signupform=Createsignup()
        return render(request,"signup.html",{"signupform":signupform})
def signin(request):
    if request.method == 'POST':
        myid=request.POST.get('myid')
        pw=request.POST.get('pw')
        #이건 어떤용도로 쓰이는줄 모르 겟음
        #member1=Member.objects.filter(myid=myid)
        #일단 이거 써야 얻을수있음
        form =Createlogin(request.POST)
        print(form.is_valid())
        if form.is_valid():
            result='1';
            #return redirect(reverse('signin', kwargs={ 'result': result }))
            return render(request,'signin.html',{"result":result})
        else:
            member1 = Member.objects.get(myid=myid)
            print(member1.pw)
            # 안에 속성값 바꾸기
            # form.cleaned_data['들어온 파라미터']

            if (form.cleaned_data['pw'] == member1.pw):
                print("로긴 성공")
                print(form.cleaned_data)

                request.session['myid'] = myid
                # form.save()
                result = '3';
                return render(request, 'signin.html', {"result": result})
                #return redirect('home')
            else:
                result = '2';
                return render(request, 'signin.html', {"result": result})
    else:
        loginform=Createlogin()
        return render(request,"signin.html",{'loginform':loginform})

def oauth(request):
    code=request.GET.get('code')
    k_token_url="https://kauth.kakao.com/oauth/token"
    #전송방법1
    #?grant_type=authorization_code&" \
            # "client_id=3ebeac8272c8353cf2ff9f714fa3880d&" \
            # "redirect_uri=http://127.0.0.1:8000/oauth&" \
            # "code="+code

    #전송방법2
    a=requests.post(k_token_url,data={'grant_type':'authorization_code','client_id':'3ebeac8272c8353cf2ff9f714fa3880d',
                    'redirect_uri':'http://127.0.0.1:8000/oauth','code':code})
    #print(a)
    #print(a.text)
    #a.text 뺄수있음
    k_token=a.json()['access_token']
    request.session['k_token']=k_token
    print(k_token)
    return redirect('signin')
def k_logout(request):
    k_logout_url="https://kapi.kakao.com/v1/user/logout"
    k_token=request.session.get('k_token')
    print(k_token)
    hearders={
        "Authorization": "Bearer "+k_token
    }
    a=requests.post(k_logout_url,headers=hearders)
    print(a)
    print(a.text)
    del request.session['k_token']
    return redirect('signin')
def k_delete(request):
    k_delete_url="https://kapi.kakao.com/v1/user/unlink"
    k_token=request.session.get('k_token')
    hearders={
        "Authorization": "Bearer "+k_token
    }
    a=requests.post(k_delete_url,headers=hearders)
    print(a)
    print(a.text)
    return redirect('signin')

def select_me(request):
    k_select_me_url="https://kapi.kakao.com/v2/user/me"
    k_token = request.session.get('k_token')
    print(k_token)
    headers={
        "Authorization": "Bearer "+k_token,
        "Content-type": "application/x-www-form-urlencoded;charset = utf-8"
    }
    a=requests.get(k_select_me_url,headers=headers)
    print(a)
    print(a.text)
    return redirect('signin')
