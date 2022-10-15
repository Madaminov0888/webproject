import sys
sys.path.append('/Users/Madaminov/Desktop/web_server/parsing_data/')
import config
from django.db.models import Model
#import parsing_data.kunuz as kunuz


def get_data(model:Model) -> dict:
    h = dict()
    obj_title = model.objects.values_list('news_url')
    for title in obj_title:
        u = dict()
        obj = model.objects.filter(news_url = title[0])[0]
        u['news_name'] = obj.news_name
        u['news_count_views'] = obj.news_count_views
        u['news_text'] = obj.news_text
        u['news_date'] = obj.news_date
        h[obj.news_url] = u
    return h

#print(get_data(last_news))


