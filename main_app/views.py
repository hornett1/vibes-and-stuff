import json
import os
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
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
            cassettes = Cassette.objects.filter(is_public=True) | Cassette.objects.filter(uploader=request.user)
            print(f'Authenticated user: {request.user}, Cassettes count: {cassettes.count()}')
        else:
            cassettes = Cassette.objects.filter(is_public=True)
            print(f'Guest user, Cassettes count: {cassettes.count()}')

        paginator = Paginator(cassettes, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

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
    fields = ['title', 'author', 'color1', 'color2', 'color3', 'accent_color']
    template_name = 'main_app/cassettes-create.html'
    success_url = reverse_lazy('cassettes-list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.uploader = self.request.user
            return super().form_valid(form)
        else:
            return HttpResponseForbidden("You must be logged in to create a cassette.")

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

class CassettesUpdateView(UpdateView):
    model = Cassette
    context_object_name = 'cassette'
    fields = '__all__'
    template_name ='main_app/cassettes-update.html'
    success_url = reverse_lazy('cassettes-list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.uploader = self.request.user
        else:
            return HttpResponseForbidden("You must be logged in to create a cassette.")
        
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        """ Обрабатывает AJAX-запрос и сохраняет изменения. """
        cassette = get_object_or_404(Cassette, pk=kwargs["pk"])

        if not request.user.is_authenticated:
            return JsonResponse({"error": "Unauthorized"}, status=403)

        try:
            data = json.loads(request.body)
            if "title" in data:
                cassette.title = data.get("title", cassette.title)

            if "author" in data:
                cassette.author = data.get("author", cassette.author)

            if "is_public" in data:
                cassette.is_public = data.get("is_public", cassette.is_public)
            cassette.save()
            return JsonResponse({"status": "success", "new_data": {
                "title": cassette.title,
                "author": cassette.author,
                "is_public": cassette.is_public,
            }})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

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

class SongsUpdateView(UpdateView):
    model = Song
    context_object_name = 'song'
    template_name ='main_app/songs-update.html'
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


