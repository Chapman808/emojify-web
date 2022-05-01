from django.urls import path

from . import views
from .views import RunProfilePicEmojify, SubmitDoodleEmojify
urlpatterns = [
    path('', views.index, name='index'),
    path('api/server-emojis/', RunProfilePicEmojify.as_view(), name='api/server-emojis/'),
    path('api/submit-doodle/', SubmitDoodleEmojify.as_view(), name='api/server-emojis/'),
]