import os
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.views import View
from auth_app.models import User
from .models import Song, Cassette
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView
from django.core.paginator import Paginator

class MainPageTemplate(TemplateView):
    template_name = 'main-page.html'

class CassetteListView(View):
    template_name = 'main_app/cassettes.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Получаем кассеты, доступные для публичного просмотра или принадлежащие текущему пользователю
            cassettes = Cassette.objects.filter(is_public=True) | Cassette.objects.filter(uploader=request.user)
            print(f'Authenticated user: {request.user}, Cassettes count: {cassettes.count()}')
        else:
            # Получаем только публичные кассеты для неавторизованных пользователей
            cassettes = Cassette.objects.filter(is_public=True)
            print(f'Guest user, Cassettes count: {cassettes.count()}')

        paginator = Paginator(cassettes, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Печать для отладки
        print(cassettes)

        context = {
            'cassettes': cassettes,
            'page_obj': page_obj,
        }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return render(request, 'main_app/cassettes-list.html', context=context)
        
        return render(request, self.template_name, context)
    
class CassetteCreateView(CreateView):
    model = Cassette
    context_object_name = 'cassette'
    fields = '__all__'
    template_name = 'main_app/cassettes-create.html'
    success_url = reverse_lazy('cassettes-list')

    def form_valid(self, form):
        # Устанавливаем uploader равным текущему авторизованному пользователю
        if self.request.user.is_authenticated:
            form.instance.uploader = self.request.user
        else:
            return HttpResponseForbidden("You must be logged in to create a cassette.")
        
        return super().form_valid(form)

    # def form_valid(self, form):
    #     messages.success(self.request, "Cassette added successfully.")
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     title = form.cleaned_data.get('title', '')
    #     author = form.cleaned_data.get('author', '')

    #     if len(title) > 50:
    #         form.add_error('title', 'Title should be less than 50 characters.')

    #     if len(author) > 50:
    #         form.add_error('author', 'Author should be less than 50 characters.')

    #     if len(title) > 50:
    #         messages.error(self.request, "Title should be less than 50 characters.")
        
    #     if len(author) > 50:
    #         messages.error(self.request, "Author should be less than 50 characters.")

    #     return super().form_invalid(form)

class CassettesDeleteView(DeleteView):
    model = Cassette
    context_object_name = 'cassette'
    template_name ='main_app/cassettes-delete.html'
    success_url = reverse_lazy('cassettes-list')

class SongsCreateView(CreateView):
    model = Song
    context_object_name = 'song'
    fields = ['title', 'author', 'source']
    template_name = 'main_app/songs-create.html'
    success_url = reverse_lazy('cassettes-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cassette'] = get_object_or_404(Cassette, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.cassette = get_object_or_404(Cassette, pk=self.kwargs['pk'])
        if not self.request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in to upload a song.")
        return super().form_valid(form)
    
class SongsDeleteView(DeleteView):
    model = Song
    context_object_name = 'song'
    template_name ='main_app/songs-delete.html'
    success_url = reverse_lazy('cassettes-list')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in to upload a song.")
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.get_object()
        context['cassette'] = song.cassette
        return context


