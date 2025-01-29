from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment, Image


class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = "gallery_app/images.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Получаем кассеты, доступные для публичного просмотра или принадлежащие текущему пользователю
            images = Image.objects.filter(is_public=True) | Image.objects.filter(author=request.user)
            print(f'Authenticated user: {request.user}, images count: {images.count()}')
        else:
            # Получаем только публичные кассеты для неавторизованных пользователей
            images = Image.objects.filter(is_public=True)
            print(f'Guest user, images count: {images.count()}')

        paginator = Paginator(images, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Печать для отладки
        print(images)

        context = {
            'images': images,
            'page_obj': page_obj,
        }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return render(request, 'main_app/images-list.html', context=context)
        
        return render(request, self.template_name, context)

class AddComment(SuccessMessageMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = "gallery_app/images.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('image-list')

class CreateImageView(CreateView):
    model = Image
    fields = '__all__'
    template_name = 'gallery_app/images.html'
    success_url = reverse_lazy('images-list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            return HttpResponseForbidden("You must be logged in to create an image.")
        
        image = form.save()

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'image': image.image.url, 
                'title': image.title,
            })
        
        return super().form_valid(form)


    # def form_valid(self, form):
    #     messages.success(self.request, "Image added successfully.")
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
