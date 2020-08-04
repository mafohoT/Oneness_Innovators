"""Oneness_innovators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('home/', views.home , name='home'),
    url('contact/', views.contact ,name='contact'),
    url('about/', views.about , name='about'),
    url('login/', views.login , name='login'),
    url('test/', views.test , name='test'),
    url('home2/', views.home2 , name='home2'),
    url('registration/', views.registration , name='registration'),
]
