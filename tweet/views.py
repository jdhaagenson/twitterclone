from django.shortcuts import render
from .forms import TweetForm
from .models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from django.shortcuts import HttpResponseRedirect, reverse
import re
from django.contrib.auth import get_user


# Create your views here.
def find_tags(text):
    tags = []
    for word in text.split():
        if word.startswith('@') != 0:
            tag = word[1:]
            user = TwitterUser.objects.get(username=tag)
            tags.append(tag)
    return tags


def tweet_detail(request, tweet_id):
    user = get_user(request)
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'details.html', {'tweet': tweet})


@login_required
def tweet_form(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # pattern = '(@\w+)'
            # tags = re.findall(pattern, data.get('text'))
            # text = data.get('text')
            # if tags is not None:
            #     for i in tags:
            #         tagged_user = TwitterUser.objects.get(username=i)
            #         text = text.replace(i, f'<a href=/user/{tagged_user.id}>@{i}</a>')
            text = data.get('text')
            tags = find_tags(text)
            user = get_user(request)
            new_tweet = Tweet.objects.create(
                author=user,
                text=text)
            if tags:
                for i in tags:
                    Notification.objects.create(
                        user=TwitterUser.objects.get(username=i),
                        message=new_tweet)
            return HttpResponseRedirect(request.GET.get('next', reverse("main")))
    form = TweetForm()
    return render(request, 'form.html', {'form': form})
