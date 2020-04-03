from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics,mixins
from blog.models import Post
from rest_framework.permissions import IsAdminUser


class BlogListAPIView( mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.ListAPIView):
    lookup_field = 'pk'
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id')
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            qs = qs.filter(content__icontains = query)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
