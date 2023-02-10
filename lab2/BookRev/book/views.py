from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return  HttpResponse("Main page")

def genres(request, genreid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Books by genres<h1><p>{genreid}<p>")

def archive(request,year):
    if int(year) > 2023:
        return redirect('/', permanent=True)

    return HttpResponse(f"<h1>Archive by year<h1><p>{year}<p>")

def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")