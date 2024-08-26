# import serializer from rest_framework
from rest_framework import serializers
from .models import MovieModel

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = MovieModel
		fields = ('id','title', 'description')