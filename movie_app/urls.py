from django.urls import path
from movie_app import views
urlpatterns = [
    path('', views.movie_list_api_view),
    path('<int:movie_id>/', views.movie_detail_api_view),
    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorListAPIView.as_view()),
    path('movies/', views.MovieListAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('movie_review/', views.MovieReviewListAPIView.as_view()),
    path('review/', views.ReviewListAPIView.as_view()),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
]
