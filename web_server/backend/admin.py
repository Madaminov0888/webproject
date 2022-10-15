from django.contrib import admin
from .models import Last_news, Popular_news


@admin.register(Last_news)
class news_admin(admin.ModelAdmin):
    list_display = ['news_name', 'news_url', 'news_date']

@admin.register(Popular_news)
class news_admin(admin.ModelAdmin):
    list_display = ['news_name', 'news_url', 'news_date']


