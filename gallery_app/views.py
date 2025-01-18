from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm
from .models import Comment, Image

class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = "gallery_app/images.html"

class AddComment(SuccessMessageMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = "gallery_app/images.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('image-list')

class CreateImageView(CreateView):
    model = Image
    context_object_name = 'image'
