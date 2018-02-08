'''
Created on Feb 7, 2018

@author: vp60132n
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")