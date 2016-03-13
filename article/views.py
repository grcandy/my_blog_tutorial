# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from django.shortcuts import render
from django.http.response import HttpResponse
import datetime

def home(request):
    return HttpResponse("Hello Django!!")

def now_time(request):
    return render(request, "time.html", {"current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

