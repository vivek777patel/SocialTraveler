'''
Created on Feb 7, 2018

@author: vp60132n
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
