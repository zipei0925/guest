from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # return HttpResponse("Hello Django")
    return render(request, "index.html")


# 登录动作
def login_action(requst):
    if requst.method == 'POST':
        username = requst.POST.get('username', '')
        password = requst.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) # 通过auth_user表中数据进行验证
        # 用户名和密码正确返回user对象,否则返回None
        if user is not None:
            auth.login(requst, user) # login()函数接受HttpRequest对象和user对象登录
            response = HttpResponseRedirect('/event_manage/')  # 登录成功后重定向至路径/event_manage/
            # response.set_cookie('user',username,3600)  # 添加浏览器cookie ('cookie名称',用户名,生效时长 )
            requst.session['user'] = username  # 将 session 信息记录到浏览器
            return response
        else:
            return render(requst, 'index.html', {'error': 'username or passwword error!'})


# 发布会管理
@login_required()
def event_manage(requst):
    # username = requst.COOKIES.get('user', '') # 读取浏览器cookie名为"user"的值
    username = requst.session.get('usr', '')  # 读取浏览器session名为"user"的值
    return render(requst, 'event_manage.html', {"user": username})  # 返回event_manage页面和cookie值
