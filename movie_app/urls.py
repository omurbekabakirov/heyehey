from django.urls import path
from movie_app import views
urlpatterns = [
    path('', views.movie_list_api_view),
    path('<int:movie_id>/', views.movie_detail_api_view),
]
