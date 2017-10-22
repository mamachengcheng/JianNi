# **coding: utf-8**
import sys
from rest_framework.views import APIView, Response
from chat.models import User
from utils.cache import get_cache_redis
from django.http import HttpResponse
import json


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
        for user in users:
            card = dict()
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
        print content
        # return Response(data=content)
        return HttpResponse(json.dumps(content))


class AddTagAPIView(APIView):

    """
    添加tag
    """

    def get(self, request):
        tag = request.GET.get('tag')
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        weibo_name = user.weibo_name
        cache = get_cache_redis()
        cache.sadd(weibo_name, tag)
        content = dict()
        content['state_code'] = 100
        content['message'] = "设置成功"
        return Response(data=content)


class DeleteTagAPIView(APIView):

    """
    删除tag
    """

    def get(self, request):
        tag = request.GET.get('tag')
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        weibo_name = user.weibo_name
        cache = get_cache_redis()
        cache.srem(weibo_name, tag)
        content = dict()
        content['state_code'] = 100
        content['message'] = "设置成功"
        return Response(data=content)
