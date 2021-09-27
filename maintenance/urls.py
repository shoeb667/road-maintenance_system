"""maintenance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('home',views.home,name="home"),
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_login',views.user_login,name='user_login'),
    path('submit_issue',views.submit_issue,name='submit_issue'),
    path('check',views.check,name="check"),
    path('maintenance',views.maintenance,name="maintenance"),
    path('maintenance1',views.maintenance1,name="maintenance1"),
    path('maintenance2',views.maintenance2,name="maintenance2"),
    path('maintenance3',views.maintenance3,name="maintenance3"),
    path('contactus_form',views.contactus_form,name="contactus_form"),
    path('user_home',views.user_home,name='user_home'),
]

