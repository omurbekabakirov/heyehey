from django.urls import path
from user import views
urlpatterns = [
    path('registration/', views.registration_api_view),
    path('authorization/', views.authorization_api_view),
    path('get_code/',views.send_confirm_code_api_view),
    path('confirm_code/', views.confirm_email_api_view)
]
