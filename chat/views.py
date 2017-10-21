# **coding: utf-8**
import sys
from rest_framework.views import APIView, Response
from .models import User, Friend
from .serializers import FriendListSerializer
from utils.cache import get_cache_redis


reload(sys)
sys.setdefaultencoding('utf8')


class AddFriendAPIView(APIView):

    """
    建立聊天
    """

    def get(self, request):
        user_id = request.GET.get('user_id')
        friend_id = request.GET.get('friend_id')
        user = User.objects.get(id=user_id)
        friend = Friend(
            User=user,
            friend_id=friend_id,
            last_message=''
        )
        friend.save()
        content = dict()
        content['state_code'] = 100
        content['message'] = "添加成功"
        return Response(data=content)


class DeleteFriendAPIView(APIView):

    """
    删除聊天
    """

    def get(self, request):
        user_id = request.GET.get('user_id')
        friend_id = request.GET.get('friend_id')
        friend = Friend.objects.filter(User=user_id).get(friend_id=friend_id)
        friend.delete()
        content = dict()
        content['state_code'] = 100
        content['message'] = "删除成功"
        return Response(data=content)


class FriendListAPIView(APIView):

    """
    好友类表
    """

    def get(self, requst):
        user_id = requst.GET.get('user_id')
        friends = Friend.objects.filter(User=user_id).all()
        serializer = FriendListSerializer(friends, many=True)
        content = dict()
        content['items'] = serializer.data
        return Response(data=content)

