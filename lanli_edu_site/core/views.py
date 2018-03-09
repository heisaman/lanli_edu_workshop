from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello World!<br/>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    return render(request, "core/index.html")


def seminar(request):
    return render(request, "core/seminar.html")


def interaction(request):
    return render(request, "core/interaction.html")


def home(request):
    return render(request, "core/home.html")
