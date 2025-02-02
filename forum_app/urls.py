from django.urls import path
from .views import AddMessage, TopicCreateView, TopicListView, ArticleListView, ArticleCreateView

urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('topics/add/', TopicCreateView.as_view(), name='topic-add'),
    path('articles/<int:pk>/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/add/', ArticleCreateView.as_view(), name='article-add')
    # path('themes/<int:pk>/', TopicListView.as_view(), name='theme-detail'),
]