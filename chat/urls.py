# **coding: utf-8**
import views
from django.conf.urls import url

urlpatterns = [
    url(r'AddFriendAPIView', views.AddFriendAPIView.as_view()),
    url(r'DeleteFriendAPIView', views.DeleteFriendAPIView.as_view()),
    url(r'FriendListAPIView', views.FriendListAPIView.as_view()),
]
