from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainPageTemplate.as_view(), name='main-page'),
    path('cassettes/', CassetteListView.as_view(), name='cassettes-list'),
    path('cassettes/create/', CassetteCreateView.as_view(), name='create-cassette'),
    path('cassettes/<int:pk>/delete/', CassettesDeleteView.as_view(), name='delete-cassette'),
    path('songs/<int:pk>/create/', SongsCreateView.as_view(), name='create-song'),
    path('songs/<int:pk>/delete/', SongsDeleteView.as_view(), name='delete-song'),
]
