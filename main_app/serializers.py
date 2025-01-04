from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):    
    uploader_name = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = '__all__'

    def get_uploader_name(self, obj):
        return obj.uploader.username if obj.uploader else "Unknown"
