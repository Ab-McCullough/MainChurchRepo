from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def main_page(request: HttpRequest)->render:
    return render(request, 'index.html')
def event_page(request: HttpRequest)->render:

    return render(request, "events.html")