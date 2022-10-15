from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Last_news, Popular_news
from parsing_data.data_updater import get_data


def last_news_func(request):
    return JsonResponse(get_data(Last_news))
    #return HttpResponse('<h1>Hello</h1>')

def popular_news_func(request):
    return JsonResponse(get_data(Popular_news))
    