from django.shortcuts import render
from django.views.generic.list import ListView
from mediaportalapp.models import Article
#def index(request):
    #return render(request, 'mediaportalapp/article.html')
class ArtcileListView(ListView):
    model = Article
    template_name = 'articles.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArtcileListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context
# Create your views here.
