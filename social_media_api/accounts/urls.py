from django.urls import path
from .views import register_user, login_user, user_profile

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('profile/', user_profile, name='user_profile'),
]