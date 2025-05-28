from django.urls import path

from insta_loader.views import VideoView, ReelsView, PhotoView, StoryView

app_name = 'insta_loader'
urlpatterns = [
    path("", VideoView.as_view(), name="video"),
    path("story", StoryView.as_view(), name="story"),
    path("photo", PhotoView.as_view(), name="photo"),
    path("reels", ReelsView.as_view(), name="reels"),
]
