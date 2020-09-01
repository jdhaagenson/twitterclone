from django.shortcuts import render
from .forms import TweetForm
from .models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


# Create your views here.
def tweet_detail(request):
    pass


def tweet_form(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data


    form = TweetForm()
    return render(request, 'form.html', {'form': form})


def find_tags(text):
    for word in text.split():
        if word.startswith('@') != 0:
            tag = word[1:]
            user = TwitterUser.objects.get(username=tag)



