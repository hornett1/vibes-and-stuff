from django.db import models
from auth_app.models import User

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
