from django.urls import path
from videos import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('video/<int:id>', views.VideoView.as_view(), name='video'),
    path('video/<int:id>/download', login_required(views.DownloadVideoView.as_view()), name='download-video'),
    path('deovr/<int:id>', views.DeoVRVideoView.as_view(), name="deovr-video"),
    path('deovr', views.DeoVRVideosView.as_view(), name='deovr'),
]
