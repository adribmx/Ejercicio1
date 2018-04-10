from django.contrib import admin
from tweets.models import Tweet
from tweets.models import User

class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_text', 'pub_date', 'get_user_nick']
    def get_user_nick(self, obj):
        return obj.user.nick
    get_user_nick.short_description = 'User Nick'
    get_user_nick.admin_order_field = 'user__nick'

class UserAdmin(admin.ModelAdmin):
    list_display = ['nick', 'join_date']

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
