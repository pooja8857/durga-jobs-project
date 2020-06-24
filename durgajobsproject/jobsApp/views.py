from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hydjobsinfo(request):
    s = '<h1>Hydrabad jobs information</h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s = '<h1>pune jobs information</h1>'
    return HttpResponse(s)


def mumbaijobsinfo(request):
    s = '<h1>mumbai jobs information</h1>'
    return HttpResponse(s)


def channaijobsinfo(request):
    s = '<h1>channai jobs information</h1>'
    return HttpResponse(s)
