from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'songs', SongCRUDView, basename='songs-crud')
router.register(r'cassettes', CassetteCRUDView, basename='cassettes-crud')

urlpatterns = [
    path('songs-list/', SongListView.as_view(), name='songs-list'),
    path('register/', RegistraionAPIView.as_view(), name='register'), 
    path('login/', LoginAPIView.as_view(), name='login'),
    path('current-user/', GetCurrentUserAPIView.as_view(), name='current_user'),
    path('', include(router.urls)),
]
