from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import  CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post

def blog_list(request):
	context = {
		'title': 'some title here',
		'description': 'some description as well'
	}
	return JsonResponse(context)
# Create your views here.
def blogg(request):
    return render(request, 'blog/comments.html', {
    'post': Post.objects.all()
    })

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'description']

  def form_valid(self, form):
    return super().form_valid(form)
