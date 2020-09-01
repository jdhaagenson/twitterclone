"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from twitteruser.views import *
from notification.views import *
from tweet.views import *
from authentication.views import *

urlpatterns = [
    path('/', main, name='main'),
    path('login/', twitter_login, name='twitter_login'),
    path('logout/', twitter_logout, name='twitter_logout'),
    path('tweet/<int:tweet_id>/', tweet_detail, name='tweet_detail'),
    path('user/<int:userid>', profile, name='profile'),
    path('notifications/', notifications, name='notifications'),
    path('tweet/', tweet_form, name='tweet_form'),
    path('follow/', follow, name='follow'),
    path('unfollow/', unfollow, name='unfollow'),
    path('register/', registration_form, name='register'),
    path('admin/', admin.site.urls),

]
