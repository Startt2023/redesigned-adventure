#encoding=utf-8
from django.contrib import admin
from django.urls import path,include
#from  app import index
from . import views
urlpatterns = [
    #访问http://127.0.0.1/app,,,看到app就会去找view.index页面
    #path('app',view.index)
    path('index/',views.index)
]