from django.db import models
from auth_app.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model): #section
    title = models.CharField(max_length=100)

class Article(models.Model): #theme
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(max_length=10000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model): #message
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = RichTextUploadingField(max_length=10000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,)


