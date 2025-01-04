from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'songs', SongCRUDView, basename='songs-crud')

urlpatterns = [
    path('songs-list/', SongListView.as_view(), name='songs-list'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),  
    path('', include(router.urls)),
]
