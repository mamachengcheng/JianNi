# **coding: utf-8**
import views
from django.conf.urls import url

urlpatterns = [
    url(r'IndexCardAPIView', views.IndexCardAPIView.as_view()),
    url(r'AddTagAPIView', views.AddTagAPIView.as_view()),
    url(r'DeleteTagAPIView', views.DeleteTagAPIView.as_view()),

]
