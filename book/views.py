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

def pageNotFound(reguest, exeption):
    return HttpResponseNotFound('<h1>Page not found!<h1>')