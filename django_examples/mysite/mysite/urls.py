"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from mainApp.views import login_view, register_view,logout_view
from django.conf.urls.static import static
from django.conf import settings
from blog.views import blog_list, blogg, PostCreateView
from blog.api.views import BlogListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webexample/', include('webexample.urls')),
    path('', include('mainApp.urls')),
    path('', home),
    path('mainApp/login/', login_view),
    path('mainApp/signup/', register_view),
    path('mainApp/logout/', logout_view),
    path('mainApp/', include('mainApp.urls')),
    path('mediaportalapp/', include('mediaportalapp.urls')),
    path('blogg/', blogg),
    path('blogs/', blog_list),
    path('api/', BlogListAPIView.as_view()),
    path('post/new/', PostCreateView.as_view(), name='post-create'),


]

if settings.DEBUG:
    urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
