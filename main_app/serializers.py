from rest_framework import serializers
from rest_framework.authentication import authenticate
from .models import *

class SongSerializer(serializers.ModelSerializer):    
    uploader_name = serializers.SerializerMethodField()
    cassette_id = serializers.IntegerField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'author', 'uploader', 'cassette_id', 'cassette', 'uploader_name', 'source']

    def get_uploader_name(self, obj):
        return obj.uploader.username if obj.uploader else "Unknown"
    
    def create(self, validated_data):
        cassette_id = validated_data.get('cassette_id')
        print(f"cassette_id received: {cassette_id}")
        song = Song.objects.create(**validated_data)

        return song
    
class CassetteSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Cassette
        fields = '__all__'

    def create(self, validated_data):
        songs_data = validated_data.pop('songs', [])
        cassette = Cassette.objects.create(**validated_data)
        
        for song in songs_data:
            song.cassette = cassette
            song.save()
        
        return cassette

    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
            )
        return user
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Неверные имя пользователя или пароль")

        return {'user': user}
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

