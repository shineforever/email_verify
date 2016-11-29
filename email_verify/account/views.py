from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.

def error(request):
    msg = "Your E-mail address have already existed! Please return and change your E-mail address."
    return render_to_response('display.html',locals())

