from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import School, Grade, Class, Lecture, LanliUser, Notification


def hello(request):
    now = datetime.now()
    html = "<html><body>Hello World!<br/>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    return render(request, "core/index.html")


def seminar(request):
    return render(request, "core/seminar.html")


def lectures(request):
    valid_lectures = Lecture.objects.filter(expired_time__gt=datetime.now())
    expired_lectures = Lecture.objects.filter(expired_time__lt=datetime.now())
    return render(request, "core/lectures.html",
                  {"valid_lectures": valid_lectures, "expired_lectures": expired_lectures})


def interaction(request):
    return render(request, "core/interaction.html")


def home(request):
    return render(request, "core/home.html")
