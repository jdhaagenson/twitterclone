from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Notification
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def check_notifications(request):
    user = get_user(request)
    notes = Notification.objects.filter(user=user).order_by('-message__date')
    response = render_to_response('notifications.html', {'user':user, 'notifications':notes})
    return render(request, 'notifications.html', {'user': user, 'notifications': notes})


@login_required
def status_notification(request):
    if Notification.objects.get(user=get_user(request)):
        return True


@login_required
def get_notifications(request):
    user = get_user(request)
    count = Notification.objects.filter(user=user).count()
    messages = Notification.objects.filter(user=user).order_by('-message__date')
    notify_dict = {'count': count, 'messages': messages}
    return notify_dict