from django.conf.urls import url
from tweets import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<nick>\w+)/$', views.user_tweets, name='user_tweets'),
    url(r'^detail/(?P<tweet_id>\d+)/$', views.tweet_detail, name='tweet_detail'),
    ]
