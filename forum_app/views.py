from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import MessageForm
from .models import Message, Topic, Article

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    paginate_by = 10

    template_name = 'forum_app/topics.html'

class TopicCreateView(CreateView):
    model = Topic
    fields = ['title']
    success_url = reverse_lazy('topic-list')

    template_name = 'forum_app/topics.html'

class ArticleListView(DetailView): # articles in exact topic
    model = Topic
    context_object_name = 'topic'
    paginate_by = 10

    template_name = 'forum_app/articles.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.related_topic.all()
        return context
    
class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'

    def get_success_url(self):
        return reverse('article-list', kwargs={'pk': self.object.pk})

    template_name = 'forum_app/topics.html'

class ThemeDetailView(DetailView):
    model = Article
    context_object_name = "articles"
    template_name = "forum_app/theme_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.related_article.all()
        return context

class AddMessage(SuccessMessageMixin, CreateView):
    form_class = MessageForm
    model = Message
    template_name = "gallery_app/images.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('')