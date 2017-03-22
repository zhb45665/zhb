#!/bin/python
# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from datetime import datetime
from Web.models import userInfo
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def UserInfo(request):
#     伪视图
#     post = userInfo(id = '1', username = 'test', sex = 'F', info = 'only test',timestamp = datetime.now())
#     真视图
    posts = userInfo.objects.all()
    return render_to_response('index.html', {'posts' : posts})
@csrf_exempt
def create(request):
    print("ddddddddddd")
    if request.method == 'post':
        print("ddddddddddd")
        userInfo(
            id = request.post.get('id'),
            username = request.post.get('username'),
            sex = request.post.get('sex'),
            info = request.post.get('info'),
            timestamp = datetime.now(),
            ).save()
    return HttpResponseRedirect('/UserInfo/')
#     return render_to_response('index.html', {'posts' : posts}, RequestContext(request))