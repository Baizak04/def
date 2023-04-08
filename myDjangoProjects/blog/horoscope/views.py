from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def leo(request):
    return HttpResponse("Знак зодиака лев")

def scorpio(request):
    return HttpResponse("Знак зодиака Скорпион")


def get_info_about_sign_zodiac(request, sign_zodiac):
    return HttpResponse("")