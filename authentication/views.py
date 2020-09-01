from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from twitteruser.models import TwitterUser
from django.contrib.auth import login, logout, authenticate, get_user

# Create your views here.
def twitter_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('username'),
                                password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('main')))
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


def twitter_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(username=data.get('username'),
                                            password=data.get('password'),
                                            email=data.get('email'))
    form = RegistrationForm()
    return render(request, 'form.html', {'form': form})
