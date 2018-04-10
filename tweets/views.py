from django.shortcuts import render
from django.http import HttpResponse, Http404
from tweets.models import Tweet

def index(request):
    #tweet_list = Tweet.objects.order_by('-pub_date')[:10] 
    #lista = []
    #for tweet in tweet_list:
    #    lista.append(tweet.tweet_text + " por " + tweet.user.nick + "<br/>")
    #output = ''.join(lista)
    #return HttpResponse(output)

    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:5]
    context = {'latest_tweet_list': latest_tweet_list}
    return render(request, 'index.html', context)

def user_tweets(request, nick):
        return HttpResponse("Este es el timeline de %s" % nick)

def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404("El tweet no existe")
    context = {'tweet': tweet}
    return render(request, "tweets/detail.html", context)
