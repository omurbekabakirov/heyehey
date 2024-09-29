from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = 'id text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(default=0)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = 'name'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer()

    class Meta:
        model = models.Movie
        fields = 'id title directors reviews film_rating'.split()
        depth = 1

    def get_reviews(self, movie):
        return [review.text for review in movie.reviews.all()]

    def film_rating(self, movie):
        film_rating = (sum([review.star for review in movie.reviews.all()]) / len([review.star for review in movie.reviews.all()]))
        return film_rating


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    directors = serializers.ListField(child=serializers)
    duration = serializers.IntegerField()
