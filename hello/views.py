from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("""<!doctype html><html><head></head><body><h1>Добро пожаловать</h1><title>Учим django</title><a href="/hello/about">О нас</a></body></html>""")


def about(request):
    return HttpResponse("""<!doctype html><html><head></head><body><h1>Резюме: Сем</h1><title>О нас</title><a href="/hello">Главная</a></body></html>""")
