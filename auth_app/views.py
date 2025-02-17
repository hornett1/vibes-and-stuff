import os
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView, UpdateView
from .models import User
from .forms import UserCreateForm, UserAuthForm, UserBannerUpdateForm, UserAvatarUpdateForm
from main_app.models import Cassette
from gallery_app.models import Image

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main-page')

class RegisterView(FormView):
    template_name = 'auth_app/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Form is not valid.")
        return super().form_invalid(form)

class LoginView(FormView):
    template_name = 'auth_app/login.html'
    form_class = UserAuthForm
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            print("login")
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid login or password')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    
class ProfileView(DetailView):
    model = User
    template_name = 'auth_app/profile.html'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile_user'] = user
        context['cassettes'] = Cassette.objects.filter(uploader=user)
        context['images'] = Image.objects.filter(author=user)
        return context
    
class BannerUpdateView(UpdateView):
    model = User
    form_class = UserBannerUpdateForm
    template_name = 'auth_app/banner_update.html'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profile_user'] = user
        return context
    
    def form_valid(self, form):
        user = self.get_object()
        
        if user.banner and user.banner.name:
            old_banner_path = os.path.join(settings.MEDIA_ROOT, user.banner.name)
            if os.path.exists(old_banner_path):
                os.remove(old_banner_path)
        return super().form_valid(form)

    success_url = reverse_lazy('main-page')

class AvatarUpdateView(UpdateView):
    model = User
    form_class = UserAvatarUpdateForm
    template_name = 'auth_app/avatar_update.html'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profile_user'] = user
        return context
    
    def form_valid(self, form):
        user = self.get_object()
        
        if user.avatar and user.avatar.name:
            old_avatar_path = os.path.join(settings.MEDIA_ROOT, user.avatar.name)
            if os.path.exists(old_avatar_path):
                os.remove(old_avatar_path)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})