from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from tweet.models import Tweet
from .models import TwitterUser
from notification.models import Notification
from tweet.views import tweet_detail, tweet_form
from notification.views import notifications
from authentication.views import twitter_login, twitter_logout, registration_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


# Create your views here.
def profile(request, userid):
    user = get_user(request)
    profile_user = TwitterUser.objects.get(id=userid)
    tweets = Tweet.objects.all().filter(author=profile_user)
    return render(request, 'profile.html', {'user': profile_user,
                                            'tweets': tweets,
                                            'tweet_count': len(tweets),
                                            'follow_count': len(profile_user.following)})


@login_required
def follow(request, userid):
    to_follow = TwitterUser.objects.get(id=userid)
    user = TwitterUser.objects.get(request.user)
    user.following.add(to_follow)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow(request, userid):
    to_unfollow = TwitterUser.objects.get(id=userid)
    user = TwitterUser.objects.get(request.user)
    user.following.remove(to_unfollow)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def main(request):
    user = get_user(request)
    profile_page = profile(request, user.id)
    tweets = Tweet.objects.filter(author=user.following)
    return render(request, 'index.html', {'profile': profile_page,
                                          'tweets': tweets})
