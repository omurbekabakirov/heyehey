from . import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from movie_app import models
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Director, Movie, Review


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def director_list_api_view(request):
    if request.method == 'GET':
        # step 1 collect the data
        directors = models.Director.objects.all()
        # step 2 reform data into queryset
        data = serializers.DirectorSerializer(directors, many=True).data
        # step 3 return response
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = serializer.validated_data.get('name')
        director = models.Director.object.create(name=name)
        director.save()
        data = serializers.DirectorSerializer(director).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class DirectorListAPIView(ListAPIView):
    serializer_class = serializers.DirectorSerializer
    queryset = Director.objects.all()


@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, director_id):
    try:
        director = models.Director.get(id=director_id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.DirectorDetailSerializer(director, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = serializer.validated_data.get('name')
        director.save()
        return Response(data=serializers.DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DirectorDetailSerializer
    queryset = Director.objects.all()
    lookup_field = 'id'


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializers.MovieSerializer(movies, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        directors = serializer.validated_data.get('directors')
        duration = serializer.validated_data.get('duration')
        movie = models.Movie.object.create(title=title, description=description, directors=directors, duration=duration)
        movie.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.MovieSerializer(movie).data)


class MovieListAPIView(ListAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = Movie.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_review_list_api_view(request):
    try:
        movies = models.Movie.objects.all()
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.MovieSerializer(movies, many=True).data
    return Response(data, status=status.HTTP_200_OK)


class MovieReviewListAPIView(ListAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = Movie.objects.all()


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_detail_api_view(request, movie_id):
    try:
        movie = models.Movie.get(id=movie_id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(movie, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        directors = serializer.validated_data.get('directors')
        duration = serializer.validated_data.get('duration')
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.MovieDetailSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieDetailSerializer
    queryset = Movie.objects.all()
    lookup_field = 'id'



@api_view(['GET ', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        data = serializers.ReviewSerializer(reviews, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        star = serializer.validated_data.get('star')
        review = models.Review.object.create(text=text, movie_id=movie_id, star=star)
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.ReviewSerializer(review).data)


class ReviewListAPIView(ListAPIView):
    serializer_class = serializers.ReviewSerializer
    queryset = Review.objects.all()


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail_api_view(request, review_id):
    try:
        review = models.Review.get(id=review_id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.ReviewDetailSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        star = serializer.validated_data.get('star')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.ReviewDetailSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewDetailAPIView(ReviewListAPIView):
    serializer_class = serializers.ReviewDetailSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'