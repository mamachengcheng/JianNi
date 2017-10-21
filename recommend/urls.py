# **coding: utf-8**
import views
from django.conf.urls import url

urlpatterns = [
    url(r'IndexCardAPIView', views.IndexCardAPIView.as_view()),
    ]
