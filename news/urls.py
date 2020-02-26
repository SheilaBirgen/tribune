from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('archives/',views.past_days_news,name = 'pastNews'),
    path('',views.news_today,name='newsToday'),
    path('search/',views.search_results,name='search_results'),
    path('article/',views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)