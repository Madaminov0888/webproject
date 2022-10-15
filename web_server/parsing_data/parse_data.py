import kunuz
import config
from bs4 import BeautifulSoup
import requests
import datetime
from django.db.models import Model
import time
from backend.models import Last_news, Popular_news





def update_url(new_urls_list = kunuz.parse_kun_uz(), popular_urls_list = kunuz.parse_popular_news()):
    new_urls_list.reverse()
    popular_urls_list.reverse()
    for url in new_urls_list:
        response = requests.get(url = url)
        soup = BeautifulSoup(response.text, features='lxml')
        title = soup.find('div', {'class':'single-header__title'}).text
        text = soup.find('div', {'class':'single-content'}).text.strip()
        views = int(soup.find('div', {'class':'view'}).text.strip())
        dattime = soup.find('div', {'class' : 'date'}).text.split('/')
        if len(dattime) < 2:
            time , date = dattime[0].strip(), f'{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}'
        else:
            time, date = dattime[0].strip(), dattime[1].strip()
        datetime1 = datetime.datetime(year = int(date.split('.')[2]), month=int(date.split('.')[1]), day=int(date.split('.')[0]), hour=int(time.split(':')[0]), minute=int(time.split(':')[1]))
        news , bol = Last_news.objects.get_or_create(news_url = str(url))
        if bol == True:
            Last_news.objects.filter(news_url = url).update(news_name = title, news_count_views = views, news_text = text, news_date = datetime1)
        else:
            Last_news.objects.filter(news_url = url).update(news_count_views = views)

    for url in popular_urls_list:
        response = requests.get(url = url)
        soup = BeautifulSoup(response.text, features='lxml')
        title = soup.find('div', {'class':'single-header__title'}).text
        text = soup.find('div', {'class':'single-content'}).text.strip()
        views = int(soup.find('div', {'class':'view'}).text.strip())
        dattime = soup.find('div', {'class' : 'date'}).text.split('/')
        time, date = dattime[0].strip(), dattime[1].strip()
        datetime1 = datetime.datetime(year = int(date.split('.')[2]), month=int(date.split('.')[1]), day=int(date.split('.')[0]), hour=int(time.split(':')[0]), minute=int(time.split(':')[1]))
        news , bol = Popular_news.objects.get_or_create(news_url = str(url))
        if bol == True:
            Popular_news.objects.filter(news_url = url).update(news_name = title, news_count_views = views, news_text = text, news_date = datetime1)
        else:
            Popular_news.objects.filter(news_url = url).update(news_count_views = views)
    print('done')

def update_others(model:Model):
    obj_urls = model.objects.values_list('news_url')
    for url in obj_urls:
        obj = model.objects.filter(news_url = url[0])[0]
        if (datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)-obj.news_date).days >= 1:
            continue
        else:
            response = requests.get(url = url[0])
            soup = BeautifulSoup(response.text, features='lxml')
            views = int(soup.find('div', {'class':'view'}).text.strip())
            obj.news_count_views = views
            obj.save()
    print('done')



while True:
    update_url()
    update_others(Popular_news)
    update_others(Last_news)
    time.sleep(7200)

