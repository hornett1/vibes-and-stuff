from django.db import models
from auth_app.models import User
from main_app.models import Base
from ckeditor_uploader.fields import RichTextUploadingField

class Image(Base):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    downloadable = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE)
    body = RichTextUploadingField(max_length=250)

