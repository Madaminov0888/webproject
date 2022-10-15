from django.urls import path
from . import views

urlpatterns=[
    path('', views.last_news_func, name = 'last-news')
]

