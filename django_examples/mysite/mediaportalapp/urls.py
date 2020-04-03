from django.urls import path, include
from mediaportalapp.views import ArtcileListView
from . import views
urlpatterns = [
    path('', ArtcileListView.as_view()),
    #path('', views.index, name="index"),
]
