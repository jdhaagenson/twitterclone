from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Notification
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth import get_user


# Create your views here.
def check_notifications(request):
    user = get_user(request)
    notes = Notification.objects.filter(user=user).order_by('message__date')
    return render(request, 'notifications.html', {'user': user, 'notifications': notes})


def status_notification(request):
    if Notification.objects.get(user=request.user):
        return True