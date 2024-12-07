from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def rules(request: HttpRequest) -> HttpResponse:
    return render(request, 'rules.html')
