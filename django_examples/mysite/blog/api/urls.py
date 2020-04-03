from .views import BlogListAPIView
from django.urls import path

urlpatterns = [
        path('', BlogListAPIView.as_view(), name='blog-list'),
]
