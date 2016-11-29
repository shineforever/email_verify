#! /usr/bin/env python
# coding: utf-8

from django.shortcuts import render,HttpResponse,render_to_response,redirect
from models import account

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
    return render_template('display.html', msg=msg)


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
    

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

        # print('token: ',token)
        # print('authcode: ', authcode)
        if token != None and authcode != None:
            redirect('success')
        else:
            return HttpResponse('OK')


