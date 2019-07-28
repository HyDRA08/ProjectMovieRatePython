"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    # login
    path('',views.valid,name="valid"),
    path('signup/',views.signupform,name="signuplink"),
    path('signupsave/',views.signup,name="signup"),
    path('login/',views.loginform,name="loginlink"),
    path('logincheck/',views.logcheck,name="loglink"),
    path('signout/',views.signout,name="signoutlink"),
    path('home/',views.home,name="homelink"),
    path('rated/',views.rated,name="ratedmovielink"),
    path('rated1',views.rated1,name="movielink"),
    path('reviewed/',views.reviewed,name="reviewlink"),
    path('profile/',views.profile,name="profilelink"),
    path('rate/',views.rate,name="ratelink"),
    path('rate1/',views.rate1,name="rate1link"),
    path('rate2/',views.rate2,name="rate2link"),
    path('newrelease/',views.release,name="releaselink"),
    path('admin/',views.admin,name="adminlink"),
    path('addmovie/',views.addmovie,name="addmovielink"),
    path('addlink',views.adding,name="addinglink"),
    path('userrating/',views.userrating,name="userratinglink"),
    path('deluser/',views.deluser,name="deleteuserlink")
]