from tabnanny import verbose
from django.db import models


class Last_news(models.Model):
    class Meta():
        verbose_name = 'Last News'
        verbose_name_plural = 'Last News'

    news_url = models.URLField(unique=True, null=True, default='https://kun.uz')
    news_name = models.CharField(null=True, default='News name', max_length=25)
    news_count_views = models.IntegerField(null=True, default=1)
    news_text = models.TextField(null=True, default='0')
    news_date = models.DateTimeField(null=True)


class Popular_news(models.Model):
    class Meta:
        verbose_name = 'Popular News'
        verbose_name_plural = 'Popular News'

    news_url = models.URLField(unique=True, null=True, default='https://kun.uz')
    news_name = models.CharField(null=True, default='News name', max_length=25)
    news_count_views = models.IntegerField(null=True, default=1)
    news_text = models.TextField(null=True, default='0')
    news_date = models.DateTimeField(null=True)