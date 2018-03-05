# coding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


# Create your views here.
# 登录页
def login(request):
    return render_to_response('login.html')


# 首页
def index(request):
    return render_to_response('index.html')


# 用户登录
def account_login(request):
    print request.POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html', {'login_err': '用户名或密码错误'})


# 用户注销
def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponse('<h1> %s had logout!</h1>' % user)


def getd(s, p, n, store):
    result = s
    if n < 1:
        return 0
    elif n == 1:
        return s * p
    else:
        for i in range(1, n+1):
            try:
                store[i]
            except IndexError:
                store[i] = getd(s, p, n, store)
                result -= store[i]
                i += 1
            print result
    return result * p

def jisuan(request):
    return render_to_response('jisuan.html')


def do_jisuan(request):
    if request.method != 'POST':
        return
    req = request.POST
    days = int(req['days'])  # days
    invest = float(req['invest'])  # T投资金额
    proportion = float(req['proportion'])  # 返利比例
    times = float(req['times'])  # t返利倍数
    sum_money = invest * times
    days_list=range(1,days+1)
    store = {}
    result = getd(sum_money, proportion, days, store)
    print result
    return render_to_response('jisuan.html',{'invest': invest, 'sum_money': sum_money, 'proportion': proportion,'days_list':days_list,'data': result})
