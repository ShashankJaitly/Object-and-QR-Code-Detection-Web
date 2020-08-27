from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.VideoFeed, name='video-feed')
]
