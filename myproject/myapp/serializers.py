from rest_framework import serializers
from .models import Artist, Work

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    class Meta:
        model = Work
        fields = '__all__'
