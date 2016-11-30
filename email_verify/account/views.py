#! /usr/bin/env python
# coding: utf-8

from django.shortcuts import render,HttpResponse,render_to_response,redirect,HttpResponseRedirect
from .models import Account
from func.assist import get_token,get_authcode
from func.process import verify_email,send_email

# Create your views here.

def error(request):
    """
    email 存在；
    :param request:
    :return:
    """
    msg = "Your E-mail address have already existed! Please return and change your E-mail address."
    return render_to_response('display.html',locals())


def success(request):
    msg = "success"
    return render_to_response('display.html',locals())

def fail(request):
    """
    邮箱激活时间太长！
    :param request:
    :return:
    """
    msg = "Too late time out!!!"
    return render_to_response('display.html',locals())

def wait_verifyed(request):
    msg = "Our verification link has sent to your email, please check your E-mail !"
    return HttpResponse(msg)


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        try:
            account = Account(name=name, email=email)
            account.save()
            account = Account.objects.get(name=name, email=email)

            id = account.id
            name = account.name
            create_time = account.create_time
            token = get_token(id,name,create_time)
            authcode = get_authcode()
            #update相关数据
            account.token = token
            account.authcode = authcode
            account.save()
            send_email(name,email,token,authcode)
            return HttpResponseRedirect('/account/wait_verifyed')
        except:
            print "name or email has wrong!"
            return HttpResponse("name or email has wrong!")

    else:
        return render_to_response('register.html')

def do_verificatin(request):
    """
    邮箱验证，获取token和authcode；
    :param request:
    :return:
    """
    if request.method == 'GET':
        token = request.GET.get('token',None)
        authcode = request.GET.get('authcode',None)
        if token != None and authcode != None and verify_email(token,authcode):
            print("success...")
            return HttpResponse('register success!!!')
        else:
            return HttpResponse('register failure!!!')


