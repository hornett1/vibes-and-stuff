from django.db import models
from auth_app.models import User
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator

class Base(models.Model):
    is_public = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

class Cassette(Base):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='Unknown')
    description = models.TextField(blank=True, null=True)
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    color1 = ColorField()
    color2 = ColorField()
    color3 = ColorField()
    accent_color = ColorField()

def get_audio_upload_path(instance, filename):
    return f'audio/{instance.cassette.title}/{filename}'

class Song(Base):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='Unknown')
    cassette = models.ForeignKey(Cassette, blank=True, null=True, on_delete=models.CASCADE, related_name='songs')
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    source = models.FileField(
        upload_to=get_audio_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'ogg', 'wav', 'flac', 'm4a'])]
    )
    
    def __str__(self):
        uploader_name = self.uploader.username if self.uploader else "Unknown uploader"
        return f'{self.title} - {self.author} uploaded by {uploader_name}'
