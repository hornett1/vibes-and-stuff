import os
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Song
from .serializers import *
from django.conf import settings

class SongListView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class SongCRUDView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.source:
            file_path = os.path.join(settings.MEDIA_ROOT, str(instance.source))
            if os.path.isfile(file_path):
                os.remove(file_path)

        instance.delete()
        
        return Response(status=204) 
    
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })


