from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import models
from rest_framework import status


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        # step 1 collect the data
        directors = models.Director.objects.all()
        # step 2 reform data into queryset
        data = serializers.DirectorSerializer(directors, many=True).data
        # step 3 return response
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = models.Director.object.create(name=name)
        director.save()
        data = serializers.DirectorSerializer(director).data
        return Response(data=data, status=status.HTTP_201_CREATED)


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
        name = request.data.get('name')
        director.save()
        return Response(data=serializers.DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializers.MovieSerializer(movies, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        directors = request.data.get('directors')
        duration = request.data.get('duration')

        movie = models.Movie.object.create(title=title, description=description, directors=directors, duration=duration)
        movie.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.MovieSerializer(movie).data)



@api_view(['GET'])
def movie_review_list_api_view(request):
    try:
        movies = models.Movie.objects.all()
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.MovieSerializer(movies, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = models.Movie.get(id=movie_id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(movie, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        directors = request.data.get('directors')
        duration = request.data.get('duration')
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.MovieDetailSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET ', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        data = serializers.ReviewSerializer(reviews, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        star = request.data.get('star')
        review = models.Review.object.create(text=text, movie_id=movie_id, star=star)
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = models.Review.get(id=review_id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.ReviewDetailSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        star = request.data.get('star')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serializers.ReviewDetailSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

