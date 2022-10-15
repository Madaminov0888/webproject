from django.urls import path
from . import views


urlpatterns = [
    path('', views.popular_news_func, name = 'popular-news-day')
]