import os
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Song, Cassette
from .serializers import *
from django.conf import settings
from django.contrib.auth import authenticate

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

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
    
class CassetteCRUDView(viewsets.ModelViewSet):
    queryset = Cassette.objects.all()
    serializer_class = CassetteSerializer

    
class RegistraionAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    model = User

    permission_classes = [AllowAny]

class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        login(request, user)

        request.session['user_id'] = user.id

        return Response({"message": "нраица"}, status=200)
    
class GetCurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except PermissionDenied:
            print("Ошибка аутентификации")
            return Response({"error": "Authentication required"}, status=403)