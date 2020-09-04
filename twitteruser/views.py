from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from tweet.models import Tweet
from .models import TwitterUser
from notification.views import get_notifications
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


# Create your views here.
def profile(request, userid):
    profile_user = TwitterUser.objects.get(id=userid)
    following = profile_user.following.all()
    tweets = Tweet.objects.all().filter(author=profile_user).order_by('-date')
    tweet_count = len(tweets)
    follow_count = len(following)
    return render(request, 'profile.html', {'user': profile_user,
                                            'tweets': tweets,
                                            'tweet_count': tweet_count,
                                            'follow_count': follow_count
                                            })


@login_required
def follow(request, userid):
    to_follow = TwitterUser.objects.get(id=userid)
    user = TwitterUser.objects.get(id=request.user.id)
    user.following.add(to_follow)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow(request, userid):
    to_unfollow = TwitterUser.objects.get(id=userid)
    user = get_user(request)
    user.following.remove(to_unfollow)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def main(request):
    user = TwitterUser.objects.get(username=request.user)
    following = user.following.all()
    tweets = Tweet.objects.filter(author__in=following)
    my_tweets = Tweet.objects.filter(author=user).values()
    tweets = tweets.union(my_tweets).order_by('-date')
    tweet_count = Tweet.objects.filter(author=user).count()
    follow_count = user.following.all().count()
    notification_count = get_notifications(request)
    return render(request, 'index.html', {'user': user,
                                          'tweets': tweets,
                                          'tweet_count': tweet_count,
                                          'follow_count': follow_count,
                                          'following': following,
                                          'notification_count': notification_count
    })
