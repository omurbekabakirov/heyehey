from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from rest_framework import status


@api_view(['GET'])
def director_list_api_view(request):
    # step 1 collect the data
    directors = models.Director.objects.all()
    # step 2 reform data into queryset
    data = serializers.DirectorSerializer(directors, many=True).data
    # step 3 return response
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_api_view(request, director_id):
    try:
        director = models.Director.get(id=director_id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.DirectorDetailSerializer(director, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = models.Movie.objects.all()
    data = serializers.MovieSerializer(movies, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = models.Movie.get(id=movie_id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.MovieDetailSerializer(movie, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET '])
def review_list_api_view(request):
    reviews = models.Review.objects.all()
    data = serializers.ReviewSerializer(reviews, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = models.Review.get(id=review_id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.ReviewDetailSerializer(review, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


