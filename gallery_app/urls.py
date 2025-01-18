from django.urls import path
from .views import AddComment, ImageListView, CreateImageView

urlpatterns = [
    path('', ImageListView.as_view(), name='image-list'),
    path('add/comment/', AddComment.as_view(), name='add-comment'),
    path('add/image/', CreateImageView.as_view(), name='add-image'),
]
