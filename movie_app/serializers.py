from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = 'name'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = 'id title directors'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = 'id text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
