from django.shortcuts import render
from .forms import TweetForm
from .models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from notification.models import Notification
import re


# Create your views here.
def tweet_detail(request):
    pass


def tweet_form(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pattern = '(@\w+)'
            tags = re.findall(pattern, data.get('text'))
            text = data.get('text')
            if tags is not None:
                for i in tags:
                    tagged_user = TwitterUser.objects.get(username=i)
                    text = text.replace(i, f'<a href=/user/{tagged_user.id}>@{i}</a>')
            new_tweet = Tweet.objects.create(
                author=request.user,
                text=text)
            if tags:
                for i in tags:
                    Notification.objects.create(
                        user=TwitterUser.objects.get(username=i),
                        message=new_tweet
                    )




    form = TweetForm()
    return render(request, 'form.html', {'form': form})


def find_tags(text):
    for word in text.split():
        if word.startswith('@') != 0:
            tag = word[1:]
            user = TwitterUser.objects.get(username=tag)



