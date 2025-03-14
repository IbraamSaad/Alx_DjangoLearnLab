from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomBookCreateView, CustomBookListView, CustomAuthorCreateView, CustomAuthorListView

router = DefaultRouter()
router.register(r'list_books', BookViewSet, basename='list_books')


urlpatterns = [
    path('', include(router.urls)),
]