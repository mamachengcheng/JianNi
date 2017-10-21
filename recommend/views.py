# **coding: utf-8**
import sys
from rest_framework.views import APIView, Response
from chat.models import User
from utils.cache import get_cache_redis


reload(sys)
sys.setdefaultencoding('utf8')


class IndexCardAPIView(APIView):

    """
    首页用户推荐好友Card
    """

    def get(self, request):
        users = User.objects.all()
        cache = get_cache_redis()
        content = dict()
        content['cards'] = []
        card = dict()
        for user in users:
            weibo_name = user.weibo_name
            cache_tags = cache.srandmember(weibo_name, 5)
            tags = []
            for tag in cache_tags:
                tags.append(tag)
            card['id'] = user.id
            card['username'] = user.username
            card['rank'] = user.rank
            card['location'] = user.location
            card['tags'] = tags
            content['cards'].append(card)

        return Response(data=content)
