from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import Notification
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


def render_callback(response):
    response.render()
    for note in response.context_data['notifications']:
        note.viewed = True
        note.save()


@login_required
def check_notifications(request):
    user = get_user(request)
    notes = Notification.objects.filter(user=user).order_by('-message__date')
    response = TemplateResponse(request, 'notifications.html', {'notifications': notes})
    response.add_post_render_callback(render_callback)
    return response


# Create your views here.
# @login_required
# def check_notifications(request):
#     user = get_user(request)
#     notes = Notification.objects.filter(user=user).order_by('-message__date')
#     render(request, 'notifications.html', {'user': user, 'notifications': notes})
@login_required
def get_notifications(request):
    user = get_user(request)
    count = Notification.objects.filter(user=user)
    count = count.filter(viewed=False).count()
    return count