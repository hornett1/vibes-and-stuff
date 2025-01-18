from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView
from .models import User
from .forms import UserCreateForm, UserAuthForm

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
        context['current_user'] = self.request.user
        context['user'] = user
        return context