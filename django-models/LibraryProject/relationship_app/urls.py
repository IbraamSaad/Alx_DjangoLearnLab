from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

login_view = LoginView.as_view(template_name='relationship_app/login.html')
logout_view = LogoutView.as_view(template_name='relationship_app/logout.html')

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]