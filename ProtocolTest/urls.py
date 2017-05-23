"""ProtocolTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from game_app import views as game_views
urlpatterns = [
    url(r'^$', game_views.index),
    url(r'^testpost1/$', game_views.testpost1, name='testpost1'),
    url(r'^testpost2/$', game_views.testpost2, name='testpost2'),
    url(r'^add/$', game_views.add, name='add'),
    url(r'^add2/$', game_views.add2, name='add2'),
    url(r'^getdata/$', game_views.getdata, name='getdata'),
    url(r'^admin/', include(admin.site.urls)),
]
