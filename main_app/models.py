from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


class Casette(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    # songs = models.
    color1 = ColorField()
    color2 = ColorField()
    color3 = ColorField()
    accent_color = ColorField()

class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='Unkown')
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    source = models.FileField(
        upload_to='audio/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'ogg', 'wav', 'flac', 'm4a'])]
    )

    def __str__(self):
        return f'{self.title} - {self.author} uploaded by {self.uploader.username}'
    
class Album(models.Model):
    title = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song, related_name='albums', blank=True)